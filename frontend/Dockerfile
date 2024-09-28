# Use an official Node runtime as a parent image
FROM node:20

# Set the working directory to /app
WORKDIR /app

# Copy package.json and yarn.lock to the working directory
COPY frontend/package.json frontend/yarn.lock ./

# Install the dependencies using Yarn
RUN yarn install

# Copy the remaining application files to the working directory
COPY frontend ./

# Build the application (if applicable)
RUN yarn build

# Expose port 3000 for the application
EXPOSE 3000

# Start the application
CMD ["yarn", "run", "dev"]