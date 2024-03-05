Проект самообучения

Задание

    Реализовать функционал самообучения для студентов. Для этого необходимо создать платформу, 
    которая работает только с авторизованными пользователями. На платформе необходимо предусмотреть 
    функционал разделов и материалов. Для каждого материала можно добавить тесты. Управление всеми сущностями 
    необходимо реализовать через стандартный Django admin. Проверка ответа на тест осуществляется с помощью 
    отдельного запроса на бэкенд. Реализовать либо Rest API, либо SSR с использованием Bootstrap. 
    Для реализации проекта использовать фреймворк Django.

Запуск проекта

    Склонируйте этот репозиторий к себе

    В файле .env.sample заполните необходимые переменные окружения

    Примените миграции:
        python3 manage.py migrate

    Запустите сервер:
        python3 manage.py runserver

Документация API

    Документация API доступна после запуска сервера по адресу: http://localhost:8000/redoc/ или http://localhost:8000/docs/