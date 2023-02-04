#chose the baseImage FROM ...
FROM node

#set the working directory 
WORKDIR /app

#specify the path which docker will be applied to (root directory)
COPY package.json /app

#then install all the dependencies
RUN npm install

COPY . /app

EXPOSE 80
#start the server (multiple server based on the image)
# RUN node server.js

#start the server based on the image
CMD ["node", "server.js"]
