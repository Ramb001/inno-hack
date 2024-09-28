# Stage 1: Build the application
FROM node:18 AS builder

WORKDIR /app

COPY ./frontend/package.json ./frontend/yarn.lock ./

RUN yarn install

COPY ./frontend ./

RUN yarn build

# Stage 2: Serve the built application using NGINX
FROM nginx:latest

COPY --from=builder /app/dist /usr/share/nginx/html

COPY ./frontend/nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
