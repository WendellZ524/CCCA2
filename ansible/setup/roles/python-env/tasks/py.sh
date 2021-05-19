#!/usr/bin/env bash

docker build -t python-env /home/ubuntu/data/CCCA2/.

if [ ! -z $(docker ps --all --filter "name=python" --quiet) ]
    then
        docker stop $(docker ps --all --filter "name=python" --quiet)
        docker rm $(docker ps --all --filter "name=python" --quiet)
fi

docker create\
      -it\
      --name python\
      -v /home/ubuntu/data/CCCA2:/data/CCCA2\
      --net=host\
      python-env

docker start python