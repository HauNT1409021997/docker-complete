FROM node

WORKDIR /app

#use bind mount to install package.json file
#docker run -it -d "D:\Learning\docker complete\docker-utility\Dockerfile:/app" --name container_name image_name:tag nodejs command (npm install)

#this cmd is used for appending the cmd after the docker run 
ENTRYPOINT [ "npm" ]

#docker build -t node-util:v1.1 .