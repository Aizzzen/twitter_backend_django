# Twitter_backend_django
![action status](https://github.com/Aizzzen/twitter_backend_django/actions/workflows/github-actions.yml/badge.svg)

## <a href="https://lucid.app/lucidchart/164f361f-9f76-4375-bf24-557551398f2d/edit?invitationId=inv_50e356ce-5d36-4c81-9a5f-4df08f3e924f&page=0_0#">Ссылка на схему БД</a>

## http://127.0.0.1:8000/api/v1/swagger/ - API docs
(набор доступных url, доступно к просмотру после запуска проекта на локальной машине)

## При запуске на локальной машине, для доступа к полному функционалу добавить файл .env (backend/backend/.env) со следующими настройками:
    EMAIL_HOST=smtp.yandex.ru / smtp.gmail.com / ...
    EMAIL_HOST_USER=почта, с которой будут приходить уведомления при регистрации
    EMAIL_HOST_PASSWORD=пароль от почты
    DEFAULT_FROM_EMAIL=почта

## Реализовано:
- регистрация, с подтверждением аккаунта по почте
- авторизация по JWT токенам
- получение, добавление, редактирование и удаление твитов
- добавление множества изображений (с твитами)

Программа CI - Github Actions. </br>
Все CI задачи (джобы) можно просмотреть в .github/workflows/github-actions.yml </br>
Если Непрерывная Интеграция - <b>Continuous integration (CI)</b> - прошла успешно
будет создан Docker образ, который запушится в DockerHub (<a href='https://hub.docker.com/repository/docker/gadamurov/twitter_backend_django/general'>ссылка на Docker образ</a>). </br> 

## Ключи для DockerHub:
    DOCKER_CONTAINER_NAME - имя контейнера
    DOCKER_LOGIN - логин DockerHub
    DOCKER_TOKEN - токен авторизации на DockerHub

Добавить ключи: <repository_name> -> Settings -> Secrets and Variables -> actions -> new repository secret

