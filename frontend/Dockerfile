# Use an official Node runtime as a parent image
FROM node:16

# Set the working directory to /app
WORKDIR /app

# Copy package.json and package-lock.json to the working directory
COPY package*.json ./

# Install the dependencies
RUN npm install

# Copy the remaining application files to the working directory
COPY . .

# Build the application (if applicable, e.g., for React apps)
RUN npm run build

# Expose port 3000 for the application
EXPOSE 3000

# Start the application
CMD [ "npm", "run", "start" ]
