FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN pip install poetry

RUN poetry config virtualenvs.in-project false

RUN poetry install --with dev --no-interaction --no-ansi

COPY . /app


