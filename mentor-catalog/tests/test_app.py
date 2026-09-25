import io
import json
import os
import tempfile
import threading
import unittest
from contextlib import redirect_stdout
from http.server import ThreadingHTTPServer
from pathlib import Path
from urllib.error import HTTPError
from urllib.request import urlopen
from unittest.mock import patch
from app import Handler


class AppTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = "http://127.0.0.1:" + str(cls.server.server_port)

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=2)

    def get(self, path):
        try:
            response = urlopen(self.base + path, timeout=2)
        except HTTPError as error:
            response = error
        with response:
            return response.status, json.load(response)

    def test_health(self):
        self.assertEqual(self.get('/healthz'), (200, {'status': 'ok'}))

    def test_version(self):
        with patch.dict(os.environ, {'APP_VERSION': 'test-sha'}):
            self.assertEqual(self.get('/version'), (200, {'version': 'test-sha'}))

    def test_items(self):
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / 'items.json'
            file.write_text('[{"id": 7}]')
            with patch.dict(os.environ, {'DATA_FILE': str(file)}):
                self.assertEqual(self.get('/items'), (200, [{'id': 7}]))

    def test_missing_data_does_not_kill_liveness(self):
        with tempfile.TemporaryDirectory() as folder:
            with patch.dict(os.environ, {'DATA_FILE': str(Path(folder)/'absent.json')}):
                self.assertEqual(self.get('/items')[0], 503)
                self.assertEqual(self.get('/healthz')[0], 200)

    def test_invalid_json(self):
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / 'items.json'
            file.write_text('broken json')
            with patch.dict(os.environ, {'DATA_FILE': str(file)}):
                self.assertEqual(self.get('/items')[0], 503)

    def test_wrong_data_shape(self):
        with tempfile.TemporaryDirectory() as folder:
            file = Path(folder) / 'items.json'
            file.write_text('{}')
            with patch.dict(os.environ, {'DATA_FILE': str(file)}):
                self.assertEqual(self.get('/items')[0], 503)

    def test_unknown_path(self):
        self.assertEqual(self.get('/absent'), (404, {'error': 'not_found'}))


if __name__ == '__main__':
    unittest.main()
