## Instructions

* [<span style="color:orange">Полезные ссылки</span>](instruction%2FInfo_Dev.md)
* [<span style="color:orange">Работа с миграциями</span>](instruction%2Falembic_command.md)
---
* [<span style="color:orange">Оформление задачи</span>](https://trello.com/c/Td7tSk0V)
---
* [<span style="color:orange">Перед работой</span>](https://trello.com/c/o8L3mAuK)
---
* [<span style="color:orange">ВАЖНО! Настройка аутентификации</span>](evoll-backend%2Fauth%2FREADME.md)
---
### Запуск базы данных.
Перейдите папку с файлом docker-compose.yml\
Выполните команду:
```
docker compose up -d pg
```
Либо подключейтесь к своей локальной базе данных.\
Для этого создайте пользователя, и базу данных в своем приложении pg4admin.

Имя базы, а так же пароль и пользователь указан в конфигурации docker-compose.yml
```
CREATE USER admin WITH PASSWORD 'password';
```
```
CREATE DATABASE evoll WITH OWNER admin;
```
---
# Обновление зависимостей:

* [<span style="color:orange">Инструкция Poetry</span>](https://habr.com/ru/articles/593529/)

```
poetry install
```
---
Создайте .env файл, заполните ключи по примеру из шаблона .env.template
```dotenv
APP_CONFIG__DB__URL=postgresql+asyncpg://user:pwd@localhost:5432/app
APP_CONFIG__DB__ECHO=1
APP_CONFIG__AUTH_JWT__ALGORITHM=foobar123
APP_CONFIG__AUTH_JWT__PRIVATE_KEY_PATH=foo/jwt-bar.pem
...
...
...
```
