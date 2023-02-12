FROM node 

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

ENV PORT 80

EXPOSE ${PORT}

#start mongo image
#docker run --name mongoDB -d  mongo 

#to add the mongo container and the backend container in the same network 
#create the network docker network create network_name
#then stop two containers, use docker run -d --rm --network network-name --name container_name image_name:tag 
# to build the mongo container and the backend container 
#do not change the frontEnd api domain in the source code because the code is run on the browser which 
#does not understand the name of docker network 

#to setup volume for mongo container read the docs about the container in docker hub and find the correct workdir path to save volume
#then run the container angain docker run -d --rm --network (...) --name container_name -v volume_name:/data/data_db image_name:tag

#to setup authentication to data server you need to use different connection string to mongo with user name and password
#then in order to run container with authentication use env variable
# docker run -d --network --rm --name container_name -v volume_name:/data/dat_db -e=MONGO_INITDB_ROOT_USERNAME=username -e MONGO_INITDB_ROOT_PASSWORD=password image_name:tag


#to setup volume and bind mount for the server container 
# use docker run -d --network --rm -v "%cd%":app/logs -v serverLog:app/logs (prevent the local log file to overwrite the container log files) 
#-v /app/node_modules (prevent the local node_module file to overwrite the current log file) --name container_name image_name:tag

#keep in mind that you must include nodemon or any othe synchronous library that can help you to sync the local change in the 
#source code folder to the network. Docker does not provide the mean to synchronize the local source code changes to the localhost

#to setup the env varible username and password for mongo container 
# in the Dockerfile write ENV MONGO_USERNAME=value ENV MONGO_USERPASSWORD=value
#in the app.js file, use process.env.MONGO_USERNAME to connect the mongo container

CMD ["node", "app.js"]