# SoftEng_Project_Genilu
Visual analysis of interactions between developers

Docker container : Githubinteract Viewer


In folder /graph ,


## Build docker container

```sh
$ docker build -t fgpv/githubinteract .
```

## Run docker container 

```sh
$ docker run -p 49160:8080 -d fgpv/githubinteract
```

## Use app 

Open navigator on url : http://localhost:49160

## Docker usefull commands

```sh
$ docker ps  ## Show all containers in execution
$ docker logs <CONTAINER ID> ## Show the output of the container
$ docker kill <CONTAINER ID> ## Stop the execution 
$ docker rm <CONTAINER ID> ## Delete container
$ docker rmi <IMAGE ID> ## Delete image
```
