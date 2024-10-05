FROM python:3.12-slim

WORKDIR /app

COPY ./requirements/. .

RUN pip install -r dev.txt

COPY ./src /app