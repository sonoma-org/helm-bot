# Helm Bot v1.3 - Дискорд бот для майнкрафт серверов

Позволяет организовать гильдии на сервере дискорд.

## Как это работает?
Позволяет зарегистрировать пользователя через сервер дискорд. После чего выдает ему роль участника сервера. Администраторы с роль модератора гильдий могут создавать гильдии для игроков. У каждой гильдии есть **имя, тег и цвет**. Бот автоматически создает роли и создает форум для гильдии.

## Зависимости
1. nLogin плагин
2. LuckPerms плагин
3. База данных PostgreSQL

_**Важно!** Бот работает только с Python 3.12 или новее_

## Начало работы
Для начала работы вам нужно отредактировать `config.ini` и внести туда свои данные.

Для запуска бота введите 
```
python main.py
```

Или же создайте примерно такой dockerfile
```
FROM python:3.12.2-bookworm
COPY . /app
RUN pip install -r /app/requirements.txt
```

## Docker Compose Example
```
version: '3'
services:
  database:
    image: postgres
    ports:
      - 5432:5432
    volumes:
      - database_data:/var/lib/mysql
    environment:
      - POSTGRES_DB=DB
      - POSTGRES_USER=USER
      - POSTGRES_PASSWORD=123123
    restart: always

  helm-bot:
    environment:
      - SQL_HOST=database
      - SQL_PORT=5432
      - SQL_USER=USER
      - SQL_DATABASE=DB
      - SQL_PASSWORD=123123
      - TOKEN=YOURTOKEN
      - RCON_IP=RCONIP
      - RCON_PASSWORD=123123123
      - REG_CHANNEL_ID=123123123
      - PLAYERS_ROLE_ID=123123123
      - GUILD_ADM_ROLE_ID=123123123
    image: saddydead1/mchelmbot
    depends_on:
      - database
    restart: unless-stopped
    working_dir: /app

volumes:
  database_data:
```

