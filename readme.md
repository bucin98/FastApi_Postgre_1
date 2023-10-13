# Викторина-сервис с использованием Docker и FastAPI(Тестовое задание)

Этот проект представляет собой простой веб-сервис, который позволяет получать случайные вопросы для викторины с
публичного API и сохранять их в базе данных PostgreSQL в Docker-контейнере. Вы также найдете инструкции по сборке и
запуску этого проекта.

## Требования

Для запуска этого проекта вам понадобятся следующие компоненты:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3

## Шаг 0: Настройка контейнера(Необязательно):

1. В файле docker-compose.yml можно изменить директорию базы данных Postgres заменив "./data" на нужную:

```bash
    volumes:
      - ./data:/var/lib/postgresql/data
```

## Шаг 1: Развертывание приложения с использованием Docker

1. Склонируйте репозиторий на свой компьютер:

```bash
git clone https://github.com/bucin98/FastApi_Postgre_1
cd FastApi_Postgre_1
```

2. Сборка и запуск контейнера:

```bash
sudo docker-compose up -d
```

3. Проверить что контейнер работает:

```bash
sudo docker ps
```

## Использование приложения

Для получения вопросов для викторины, отправьте POST-запрос с указанием количества вопросов в JSON-формате.
Будет возвращен последний добавленный вопрос.

Например:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"questions_num": 1}' http://localhost:8000/api/v1/question
```

## Завершение работы

Чтобы завершить работу контейнера приложения, выполните:

```bash
docker-compose down
```