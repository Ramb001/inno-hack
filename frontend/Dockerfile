# Этап 1: Сборка приложения
FROM node:18 AS builder

WORKDIR /app

COPY ./frontend/package.json ./frontend/yarn.lock ./

RUN yarn install

COPY ./frontend ./

RUN yarn build

FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html

# Копируем пользовательский конфиг nginx
COPY ./frontend/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 3000

CMD ["nginx", "-g", "daemon off;"]