# Twitter_backend_django
![action status](https://github.com/Aizzzen/twitter_backend_django/actions/workflows/github-actions.yml/badge.svg)
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
будет создан Docker образ, который запушится в DockerHub. </br> 

## Ключи для DockerHub:
    DOCKER_CONTAINER_NAME - имя контейнера
    DOCKER_LOGIN - логин DockerHub
    DOCKER_TOKEN - токен авторизации на DockerHub

Добавить ключи: <repository_name> -> Settings -> Secrets and Variables -> actions -> new repository secret
