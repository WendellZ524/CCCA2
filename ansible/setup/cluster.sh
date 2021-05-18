#!/usr/bin/env bash

export masternode=45.113.235.61
export size=3
export user=admin
export pass=admin
export VERSION='3.1.1'
export cookie='a192aeb9904e6590849337933b000c99'

curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@${masternode}:5984/_cluster_setup  -d '{"action":"enable_cluster", "bind_address":"0.0.0.0", "username":"admin", "password":"admin", "port":"5984", "remote_node":"45.113.235.61", "node_count":"3", "remote_current_user":"admin", "remote_current_password":"admin"}'
curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@${masternode}:5984/_cluster_setup  -d '{"action":"enable_cluster", "bind_address":"0.0.0.0", "username":"admin", "password":"admin", "port":"5984", "remote_node":"45.113.234.35", "node_count":"3", "remote_current_user":"admin", "remote_current_password":"admin"}'
curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@${masternode}:5984/_cluster_setup  -d '{"action":"enable_cluster", "bind_address":"0.0.0.0", "username":"admin", "password":"admin", "port":"5984", "remote_node":"45.113.234.221", "node_count":"3", "remote_current_user":"admin", "remote_current_password":"admin"}'

curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@${masternode}:5984/_cluster_setup  -d '{"action":"add_node", "host":"45.113.234.35", "username":"admin", "password":"admin", "port":"5984"}'
curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@${masternode}:5984/_cluster_setup  -d '{"action":"add_node", "host":"45.113.234.221", "username":"admin", "password":"admin", "port":"5984"}'
curl -XGET "http://${user}:${pass}@${masternode}:5984/"
curl -X POST -H "Content-Type: application/json" http://${user}:${pass}@${masternode}/_cluster_setup -d '{"action": "finish_cluster"}'

curl -X PUT http://${user}:${pass}@${masternode}:5984/tweets
curl -X PUT http://${user}:${pass}@${masternode}:5984/tweets_test1
curl -X PUT http://${user}:${pass}@${masternode}:5984/tweets_test2

curl -X PUT -d '{
  "_id": "_design/textsearch",
  "views": {
    "keywordLocationYearCounter": {
      "reduce": "_sum",
      "map": "function (doc) {\n      emit([doc.location,doc.keyword,doc.year], 1);\n}"
    },
    "locationYearCounter": {
      "reduce": "_sum",
      "map": "function (doc) {\n      emit({location:doc.location,year:doc.year}, 1);\n}"
    }
  },
  "language": "javascript",
  "indexes": {}
}' http://${user}:${pass}@${masternode}:5984/tweets/_design/textsearch
