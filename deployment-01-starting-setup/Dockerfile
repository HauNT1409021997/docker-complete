FROM node

WORKDIR /app

COPY package.json .

RUN npm install

COPY . .

EXPOSE 80

CMD ["node", "app.js"]


#steps to deploy docker container by aws ec2
#step1: create ec2 
#step2: install docker on your virtual ec2 machine
#step3: build the docker image locally then push the image to the docker hub 
#step4: download the docker image on the ec2 then run the contaner
#step5: setup ec2 security group to allow http protocol port 80 ip 0.0.0.0 connect

#steps to update the code for aws ec2 docker image
#step1: push the new image to the docker hub
#step2: stop the container on the remote machine
#step3: run docker pull manually to get new updated image 
#step4: 