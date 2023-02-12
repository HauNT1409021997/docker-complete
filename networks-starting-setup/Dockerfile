FROM node

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 80

#in order to run http request from inside a different local host server
# change localhost to host.docker.internal(domain)

CMD ["node", "app.js"]