#!/bin/bash

# Обновление репозитория
git pull

# Остановка всех контейнеров
echo "Stopping all running containers..."
docker stop $(docker ps -aq)

# Удаление всех контейнеров
echo "Removing all containers..."
docker rm $(docker ps -aq)

# Удаление всех образов
echo "Removing all images..."
docker rmi $(docker images -q)

# Пересборка и запуск контейнеров
echo "Building and starting containers..."
docker compose up --build
