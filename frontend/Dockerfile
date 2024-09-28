FROM node:lts AS development
 
WORKDIR /app
COPY package.json /app/package.json

COPY package-lock.json /app/package-lock.json


COPY --from=build /app/dist .
 
ENTRYPOINT ["nginx", "-g", "daemon off;"]
