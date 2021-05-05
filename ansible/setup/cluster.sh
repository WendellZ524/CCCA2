#!/usr/bin/env bash

export node=45.113.235.61
export masternode=45.113.235.61
export size=3
export user=admin
export pass=admin
export VERSION='3.1.1'
export cookie='a192aeb9904e6590849337933b000c99'

curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@45.113.235.61:5984/_cluster_setup  -d '{"action":"enable_cluster", "bind_address":"0.0.0.0", "username":"admin", "password":"admin", "port":"5984", "remote_node":"45.113.235.61", "node_count":"3", "remote_current_user":"admin", "remote_current_password":"admin"}'
curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@45.113.235.61:5984/_cluster_setup  -d '{"action":"enable_cluster", "bind_address":"0.0.0.0", "username":"admin", "password":"admin", "port":"5984", "remote_node":"45.113.234.35", "node_count":"3", "remote_current_user":"admin", "remote_current_password":"admin"}'
curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@45.113.235.61:5984/_cluster_setup  -d '{"action":"enable_cluster", "bind_address":"0.0.0.0", "username":"admin", "password":"admin", "port":"5984", "remote_node":"45.113.234.221", "node_count":"3", "remote_current_user":"admin", "remote_current_password":"admin"}'

curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@45.113.235.61:5984/_cluster_setup  -d '{"action":"add_node", "host":"45.113.234.35", "username":"admin", "password":"admin", "port":"5984"}'
curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@45.113.235.61:5984/_cluster_setup  -d '{"action":"add_node", "host":"45.113.234.221", "username":"admin", "password":"admin", "port":"5984"}'
curl -XGET "http://${user}:${pass}@45.113.235.61:5984/"
curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@45.113.235.61:5984/_cluster_setup -d '{"action": "finish_cluster"}'
