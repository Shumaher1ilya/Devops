"""Read-only training service. Standard library only; not a production server."""
import json
import os
import time
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlsplit


class Handler(BaseHTTPRequestHandler):
    def log_message(self, *args):
        pass

    def do_GET(self):
        start = time.monotonic()
        path = urlsplit(self.path).path
        status = 200
        if path == "/healthz":
            body = {"status": "ok"}
        elif path == "/version":
            body = {"version": os.getenv("APP_VERSION", "dev")}
        elif path == "/items":
            try:
                body = json.loads(Path(os.getenv("DATA_FILE", "demo/items.json")).read_text())
                if not isinstance(body, list):
                    raise ValueError("Dataset must be a JSON array")
            except (OSError, ValueError, UnicodeError):
                status, body = 503, {"error": "dataset_unavailable"}
        else:
            status, body = 404, {"error": "not_found"}
        payload = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        try:
            self.wfile.write(payload)
        finally:
            print(json.dumps({"time": datetime.now(timezone.utc).isoformat(),
                              "method": "GET", "path": path, "status": status,
                              "duration_ms": round((time.monotonic()-start)*1000, 2)}),
                  flush=True)


if __name__ == "__main__":
    server = ThreadingHTTPServer((os.getenv("BIND_HOST", "127.0.0.1"),
                                 int(os.getenv("PORT", "8080"))), Handler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
