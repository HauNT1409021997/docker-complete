#to create kubernetes deloyment
#use command kubectl create deployment (object_name) test --image=(image_name) kubectdelpoyv1
#to delete the deployment use kubectl delete (deployment_name) test
#for the deployment to use the image on the remote env, you must deploy your image to docker hub then you can create the deployment based on the image

#Steps to create deployment by kubeclt
#1 build a docker image successfully then push the image to the docker hub 
#2 run kubectl create deployment command (kubectl deployment deployment_name --image=image_name)

#Steps to create a service by kubectl
#1 create a deployment object
#2 run command (kubectl expose deployment_name -type=LoadBalancer(IPtype) --port=8080(the port to which the app listens)) to create a service
#3 run command (kubectl get services) to list all services created
#4 use the cluster-ip to check the app on the browser
#5 if the service is crashed then kubernete wil automatically to create the pod for you 
#6 To scale the service run command (kubectl scale deployment/deployment_name --replicas=3(number of scaled replicas))

#Steps to update the running deployment to new image 
#1 make sure the detail code in your src code is good to run on deployment
#2 build the new docker image then push it to the docker hub (remember to use tag for multi verisons)
#3 run command (kubectl set image deployment/deployment_name container_name=image_name:tag ) to update running deployment to new image
#4 eventually reset the page to see the updated src code on prod env

#Steps to roll the deployment if there is block code delpoyed on the prod env
#1 run command (kubeclt rollout history deployment/deployment_name) to check the deployment history
#2 run commnand (kubectl rollout undo deployment/deployment_name --to-revision=2(previous deployments)) to rollback to a specific deployment before

#Steps to apply the kubectl declarative ways
#1 create a deployment.yaml file
#2 run command (kubectl apply -f=deployment.yaml)
#3 run command (kubectl delete -f=deployment.yaml -f=service.yaml) to remove the all the pods and the services

#You can also merge all the yaml files into one file then separate all deployments with syntax "---".
#Remember to put the the child deployment before the master deployment

#Steps to create pod's volumes
#pod's volumes will be lost if the pod is destroyed
#1 create the deployment and the service 
#2 in the deployment.yaml file add volume below the container 
#3 specify the name, the volume type
#4 specify mountPath in the container section


#steps to create the persisten volume
#persisten volumes will separated from the node in which the pod is currently running
#1 create the deplyment and the service 
#2 create new yaml file then specify the persistent volume like the the deployment
