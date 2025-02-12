# AQA Test task

### Установка зависимостей

> В проекте используется poetry, поэтому для установки 
> необходимо выполнить следующую команду:

`poetry install --no-root`

### Запуск проекта
> В **alluredir** можно указать директорию, в которой будут хранится результаты тестирования

`poetry run pytest --alluredir=allure-results`

## Docker
> Проект поддерживает запуск в докер контейнере

`docker-compose up tests --build` - запустить тестирование

`docker-compose up allure` - запуск Allure для просмотра отчетов