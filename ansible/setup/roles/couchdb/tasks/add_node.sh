#!/usr/bin/env bash

export masternode=$1
export node=$2
export size=$3
export user=admin
export pass=admin
export VERSION='3.1.1'
export cookie='a192aeb9904e6590849337933b000c99'

curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@${masternode}:5984/_cluster_setup  -d '{"action":"enable_cluster", "bind_address":"0.0.0.0", "username":"admin", "password":"admin", "port":"5984", "remote_node":"'${node}'", "node_count":"'${size}'", "remote_current_user":"admin", "remote_current_password":"admin"}'
if [ ${node} != ${masternode} ]
then
  curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@${masternode}:5984/_cluster_setup  -d '{"action":"add_node", "host":"'${node}'", "username":"admin", "password":"admin", "port":"5984"}'

fi
