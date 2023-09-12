# Twitter_backend_django

![action status](https://github.com/Aizzzen/twitter_backend_django/actions/workflows/github-actions.yml/badge.svg)


## Данный репозиторий это бэкенд фуллстек проекта, фронт доступен по <a href="https://github.com/Aizzzen/twitter_frontend_react_ts">ссылке</a>
## <a href="https://lucid.app/lucidchart/164f361f-9f76-4375-bf24-557551398f2d/edit?invitationId=inv_50e356ce-5d36-4c81-9a5f-4df08f3e924f&page=0_0#">Ссылка на схему БД</a>(неполную)
## <a href="https://hub.docker.com/repository/docker/gadamurov/twitter_backend_django/general">Репозиторий проекта на dockerhub</a>

## http://127.0.0.1:8000/api/v1/swagger/ - API docs
(набор доступных url, доступно к просмотру после запуска проекта на локальной машине)

## Добавить файл .env (backend/backend/.env) со следующими настройками:
    EMAIL_HOST=smtp.yandex.ru / smtp.gmail.com / ...
    EMAIL_HOST_USER=почта, с которой будут приходить уведомления при регистрации
    EMAIL_HOST_PASSWORD=пароль от почты
    DEFAULT_FROM_EMAIL=почта
    DB_HOST=localhost / 127.0.0.1
    DB_NAME=имя БД
    DB_USER=пользователь БД (например, postgres)
    DB_PASS=пароль
    DB_PORT=порт (если postgres, то 5432)

## Реализовано:
- регистрация, с подтверждением аккаунта по почте
- авторизация по JWT токенам
- получение, добавление, редактирование и удаление твитов
- добавление и удаление комментариев
- добавление множества изображений (с твитами)
- возможность редактирования своего профиля
- создание чатов
- возможность онлайн чата с другими пользователями (websocket)

Программа CI - Github Actions. </br>
Все CI задачи (джобы) можно просмотреть в .github/workflows/github-actions.yml </br>
Если Непрерывная Интеграция - <b>Continuous integration (CI)</b> - прошла успешно
будет создан Docker образ, который запушится в DockerHub (<a href='https://hub.docker.com/repository/docker/gadamurov/twitter_backend_django/general'>ссылка на Docker образ</a>). </br> 

## Ключи для DockerHub:
    DOCKER_CONTAINER_NAME - имя контейнера
    DOCKER_LOGIN - логин DockerHub
    DOCKER_TOKEN - токен авторизации на DockerHub

## Технологии:
- Django
- Django Rest Framework
- PostgreSQL
- Djoser
- JWT
- Pillow
- Celery
- Redis
- Flower
- websocket (channels[daphne])
- pytest
- django-cors-headers
- python-dotenv
- drf-yasg
