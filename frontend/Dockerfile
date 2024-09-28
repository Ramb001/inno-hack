# Stage 1: Build the application
FROM node:18 AS builder

WORKDIR /app

COPY ./frontend/package.json ./frontend/yarn.lock ./

RUN yarn install

COPY ./frontend ./

RUN yarn build

# Stage 2: Serve the built application using NGINX
FROM nginx:latest

# Copy the built files to the NGINX html directory
COPY --from=builder /app/dist /usr/share/nginx/html

# Copy your NGINX config to the appropriate location
COPY ./frontend/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
