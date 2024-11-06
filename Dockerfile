FROM python:3.12-slim

WORKDIR /app

COPY ./requirements/. .

RUN apt-get update && \
    apt-get install -y postgresql-client && \
    rm -rf /var/lib/apt/lists/* && \
    pip install --no-cache-dir -r dev.txt

COPY ./src /app

