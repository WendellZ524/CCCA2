#!/usr/bin/env bash

export node=45.113.234.35
export masternode=45.113.234.35
export size=3
export user='admin'
export pass='admin'
export VERSION='3.1.1'
export cookie='a192aeb9904e6590849337933b000c99'

docker pull ibmcom/couchdb3:${VERSION}

if [ ! -z $(docker ps --all --filter "name=couchdb${node}" --quiet) ]
    then
        docker stop $(docker ps --all --filter "name=couchdb${node}" --quiet)
        docker rm $(docker ps --all --filter "name=couchdb${node}" --quiet)
fi

docker create\
      --name couchdb${node}\
      -p 5984:5984 -p 4369:4369 -p 9100-9200:9100-9200\
      --env COUCHDB_USER=${user}\
      --env COUCHDB_PASSWORD=${pass}\
      --env COUCHDB_SECRET=${cookie}\
      --env ERL_FLAGS="-setcookie \"${cookie}\" -name \"couchdb@${node}\""\
      ibmcom/couchdb3:${VERSION}

declare -a conts=(`docker ps --all | grep couchdb | cut -f1 -d' ' | xargs -n3 -d'\n'`)
for cont in "${conts[@]}"; do docker start ${cont}; done
