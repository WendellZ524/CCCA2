#!/usr/bin/env bash

docker pull nginx:latest

if [ ! -z $(docker ps --all --filter "name=frontend" --quiet) ]
    then
        docker stop $(docker ps --all --filter "name=frontend" --quiet)
        docker rm $(docker ps --all --filter "name=frontend" --quiet)
fi

docker run\
      -d -p8080:80\
      -v /home/ubuntu/data/CCCA2/dist:/usr/share/nginx/html\
      nginx
