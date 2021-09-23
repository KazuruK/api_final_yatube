# Yatube_api
## Описание

**Небольшая** социальная сеть с записными книжками релизующая принципы **RestAPI**.
Зарегистрированные пользователи могут спокойно использовать весь функционал проекта:
- Создание и просмотр постов
- Комментирование и редактирование комментариев
- Добавление постов в администраторские группы
- Подписки на посты других пользователей

**Проект реализует авторизацию с использованием _JWT-токенов_, так что пользователи могут не волноваться за безопсность своих личных данных.**


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/KazuruK/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

## Примеры запросов к API
Все методы API задокументированны с помощью **ReDoc**.
Документацию можно посмотреть по адресу:
> redoc/
