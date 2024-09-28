# Step 1: Use Node.js base image
FROM node:18

# Step 2: Set the working directory
WORKDIR /app

# Step 3: Copy package.json and package-lock.json (or yarn.lock) to the working directory
COPY package.json ./
COPY package-lock.json ./ # If you are using npm
# COPY yarn.lock ./ # If you are using Yarn

# Step 4: Install dependencies
RUN npm install # Or RUN yarn install if you're using Yarn

# Step 5: Copy the rest of your application files to the working directory
COPY . .

# Step 6: Expose the port your app runs on (default for React is 3000)
EXPOSE 80

# Step 7: Command to run your app
CMD ["npm", "run", "dev"]
