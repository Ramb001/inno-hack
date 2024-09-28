# Этап 1: Сборка приложения
FROM node:18 AS builder

WORKDIR /app

COPY ./frontend/package.json ./frontend/yarn.lock ./

COPY ./frontend/nginx.conf /etc/nginx/nginx.conf

RUN yarn install

COPY ./frontend ./

RUN yarn build

FROM nginx:latest

COPY ./frontend/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]