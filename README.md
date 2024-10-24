# AksiyaMix: Проект на Django REST Framework

Добро пожаловать в проект **AksiyaMix** — API-приложение на базе Django Rest Framework. Для разработки и развертывания используется Docker.

## Требования

Для запуска проекта вам понадобятся следующие инструменты:

- **Python 3.12**
- **Docker** и **Docker Compose**

## Установка и запуск

Чтобы запустить проект локально, выполните следующие шаги:


### 1. Клонируйте репозиторий

```bash
git clone https://github.com/Aksiya-Mix/aksiyamix/
```

### 2. Запустите docker compose

```bash
docker compose -f docker-compose.dev.yml up --build
```

### После завершения сборки, проект будет доступен по адресу:

http://localhost:8000

## Структура проекта

Проект имеет следующую структуру:

```bash
aksiyamix/
├── src/                     # Django-приложение с реализацией API
│   └── config/              # Основные настройки проекта
├── docker-compose.dev.yml   # Файл конфигурации для Docker Compose
├── Dockerfile               # Dockerfile для сборки образа проекта
└── requirements/dev.txt     # Зависимости Python для разработки
```

Этот `README.md` содержит все необходимые инструкции для запуска проекта с использованием Python 3.12 и Docker, а также общие сведения о проекте.