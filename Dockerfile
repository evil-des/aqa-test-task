FROM mcr.microsoft.com/playwright/python:v1.50.0

WORKDIR /app

# Копируем pyproject.toml и poetry.lock
COPY pyproject.toml poetry.lock ./

RUN apt-get update && apt-get install -y openjdk-11-jre curl \
    && curl -o allure-2.21.0.tgz -L https://github.com/allure-framework/allure2/releases/download/2.21.0/allure-2.21.0.tgz \
    && tar -zxvf allure-2.21.0.tgz -C /opt/ \
    && ln -s /opt/allure-2.21.0/bin/allure /usr/local/bin/allure \
    && rm -rf allure-2.21.0.tgz

# 4. Настраиваем Poetry
ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1 \
    PYTHONUNBUFFERED=1

RUN pip install poetry
# Устанавливаем Poetry зависимости
RUN poetry install --no-root

# Копируем весь код
COPY . .
