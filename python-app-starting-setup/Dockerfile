FROM python

WORKDIR /app

COPY . /app

CMD ["python", "rng.py"]

#remove image docker rm image, conainer 
#must remove container first then image 

#remove the container automatically when container is stopped
#docker run -p 3000:80 -d --rm container_id 

#checkc image info 
#docker image inspect image_id

#copy file content into the container 
#docker cp file path/. container_name:/name

#copy container file info into file 
#docker cp container_name:/name/filename.filetype(txt, xlxs, py) file path

#create container custom name and tag
#docker run -p 3000:80 -d --rm --name custom_name image_name:tag

#run container with input from terminal
#docker run -i -t  --rm --name pythonApp(docker_name) pythonapp:2st

#start contianer with input from terminal 
#docker start -i -t  --rm --name pythonApp(docker_name) pythonapp:2st

#name the image when build image 
#docker build -t image_name:tag .