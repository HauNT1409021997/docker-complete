FROM node

WORKDIR /feApp

COPY package.json /feApp

RUN npm install

COPY . .

ENV PORT 3000

EXPOSE ${PORT}

#in order to start a react container need to use -it (interactive mode)
#docker run -d -p 3000:3000 --rm -it --name multiContainerFev1.0 image_name:tag 

CMD ['npm' 'start']
