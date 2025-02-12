FROM mcr.microsoft.com/playwright/python:v1.50.0

WORKDIR /app

# Копируем pyproject.toml и poetry.lock
COPY pyproject.toml poetry.lock ./

RUN pip install poetry
# Устанавливаем Poetry зависимости
RUN poetry install --no-root

# Копируем весь код
COPY . .
