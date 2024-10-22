# AksitaMix: Проект на Django REST Framework

Добро пожаловать в проект **AksitaMix** — API-приложение на базе Django Rest Framework. Для разработки и развертывания используется Docker.

## Требования

Для запуска проекта вам понадобятся следующие инструменты:

- **Python 3.12**
- **Docker** и **Docker Compose**

## Установка и запуск

Чтобы запустить проект локально, выполните следующие шаги:

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/Aksiya-Mix/aksiyamix/

### 2. Запустите docker compose

```bash
docker compose -f docker-compose.dev.yml up --build

### После завершения сборки, проект будет доступен по адресу:

http://localhost:8000

aksiyamix/
├── src/                     # Django-приложение с реализацией API
├── src/config/              # Основные настройки проекта
├── docker-compose.dev.yml   # Файл конфигурации для Docker Compose
├── Dockerfile               # Dockerfile для сборки образа проекта
└── requirements/dev.txt     # Зависимости Python

Этот `README.md` содержит все необходимые инструкции для запуска проекта с использованием Python 3.12 и Docker, а также общие сведения о проекте.