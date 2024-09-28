# Stage 1: Build React App
FROM node:18 AS builder

# Set working directory
WORKDIR /app

# Copy package.json and yarn.lock to install dependencies
COPY ./frontend/package.json ./frontend/yarn.lock ./

# Install dependencies
RUN yarn install

# Copy the rest of the frontend files
COPY ./frontend ./

# Build the React app
RUN yarn build

# Stage 2: Serve with Nginx
FROM nginx:latest

# Copy Nginx configuration (assuming this is the config for your app)
COPY ./frontend/nginx.conf /etc/nginx/conf.d/default.conf

# Copy the React app build from the builder stage
COPY --from=builder /app/dist /usr/share/nginx/html

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
