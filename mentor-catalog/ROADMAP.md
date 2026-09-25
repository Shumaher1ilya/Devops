# Роадмап DevOps

8 учебных недель по 10–12 часов. При полном отсутствии опыта программирования выдели еще 1–2 недели на P05. Переход определяется приемкой, а не календарем.

## Первые восемь недель

- Неделя 1: [P01 — Лаборатория и репозиторий сервиса](assignments/P01.md)
- Неделя 2: [P02 — Сервис Linux и права доступа](assignments/P02.md)
- Неделя 3: [P03 — Сетевая диагностика сервиса](assignments/P03.md)
- Неделя 4: [P04 — Веб публикация и управляемый релиз](assignments/P04.md)
- Неделя 5: [P05 — Автоматизация эксплуатации](assignments/P05.md)
- Неделя 6: [P06 — Контейнерный выпуск сервиса](assignments/P06.md)
- Неделя 7: [P07 — Стенд Compose и восстановление данных](assignments/P07.md)
- Неделя 8: [P08 — Проверяемый релиз и учебный инцидент](assignments/P08.md)

## Дальнейшие этапы

### P09 — Ansible и воспроизводимый сервер

Недели 9–11. До начала: P08.

На чистой VM разверни P04 через playbook. Второй запуск не меняет систему без причины. Конфигурационное изменение вызывает нужный handler. Сдай роль, inventory.example, PR и вывод двух запусков.

Приемка: Новая VM воспроизводит сервис; повторный запуск объясним.

- [Ansible Getting Started](https://docs.ansible.com/projects/ansible/latest/getting_started/index.html) — Inventory, подключения, первый playbook. Затем roles, templates и handlers.
### P10 — Terraform и одно облако

Недели 12–15. До начала: P09.

Создай сеть и VM в одном выбранном облаке, настрой их через Ansible. Обоснуй IAM и бюджет, покажи plan без изменений и сценарий drift. Сдай IaC, PR, схему и инструкцию удаления только учебных ресурсов. Локальный Docker provider — подготовительный бесплатный вариант.

Приемка: Среда воспроизводима; state защищен; стоимость и очистка понятны.

- [Terraform Tutorials](https://developer.hashicorp.com/terraform/tutorials) — Начать с Docker для локальной практики; затем выбранное облако. Изучить variables, outputs, state и modules.
### P11 — Kubernetes и Helm

Недели 16–20. До начала: P10 либо локальный кластер после P09.

Разверни каталог в локальном кластере. Добавь probes, requests/limits, Service и внешний доступ выбранным поддерживаемым способом. Диагностируй CrashLoopBackOff и Pending, проведи rollout/rollback. Сдай manifests, Helm chart, PR и runbook.

Приемка: Самостоятельный деплой, ограниченные права и диагностика Pod.

- [Kubernetes Basics](https://kubernetes.io/docs/tutorials/kubernetes-basics/) — Deploy, explore, expose, scale, update. После tutorial добавить probes, resources, RBAC и Helm.
### P12 — Метрики логи и алерты

Недели 21–23. До начала: P11.

Собери метрики и логи сервиса, подготовь dashboard, два алерта и runbook. Создай контролируемый сбой и проверь уведомление с маршрутом доставки в учебный канал. Задай измеримый SLI успешных HTTP-запросов, окно и учебную цель SLO.

Приемка: Алерт воспроизводимо срабатывает и исчезает после восстановления.

- [Prometheus Overview](https://prometheus.io/docs/introduction/overview/) — Модель метрик, pull, exporters и labels. Далее выполнить Getting started и первые запросы.
- [Google SRE Workbook](https://sre.google/workbook/table-of-contents/) — Разделы SLO, Monitoring, Alerting, Incident Response и Postmortem Culture. Выбирать по текущему проекту.
### P13 — PostgreSQL и надежное хранение

Недели 24–26. До начала: P12.

Замени JSON dataset на PostgreSQL либо возьми согласованное приложение с БД. Создай отдельную роль приложения, миграцию и backup. Восстанови в отдельную БД, сравни данные, измерь RTO и объясни RPO. Сдай SQL, PR и протокол restore.

Приемка: Рабочее восстановление и понятные риски миграции.

- [PostgreSQL — SQL Dump](https://www.postgresql.org/docs/current/backup-dump.html) — pg_dump и восстановление. Для начала дополнить официальным Tutorial PostgreSQL.
### P14 — Безопасность и итоговая эксплуатация

Недели 27–30. До начала: P13.

Проведи аудит своего проекта, устрани подтвержденные проблемы, проверь права и утечки секретов. Выполни релиз, отказ компонента и восстановление. Сдай PR, архитектуру, журнал инцидента и backlog улучшений с обоснованием.

Приемка: Ментор разворачивает систему по документации; менти защищает ограничения.

- [Google SRE Workbook](https://sre.google/workbook/table-of-contents/) — Разделы SLO, Monitoring, Alerting, Incident Response и Postmortem Culture. Выбирать по текущему проекту.
