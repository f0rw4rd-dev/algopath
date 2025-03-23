# Развертывание

1. Установить `Docker` и `Docker Compose`. [Инструкция](https://docs.docker.com/compose/install/)
2. В папке `envs` создать файл `.env.prod` на основе `.env.prod.example` и заполнить его актуальными переменными окружения
3. Настроить `default.conf` в папке `deploy/prod/nginx`
4. Выполнить команду `docker-compose up --build -d`, находясь в папке `deploy/prod`