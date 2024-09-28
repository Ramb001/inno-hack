# Этап 1: Сборка и запуск приложения
FROM node:18

WORKDIR /app

COPY ./frontend/package.json ./frontend/package-lock.json ./

RUN npm install

COPY ./frontend ./

CMD ["npm", "run", "dev"]
