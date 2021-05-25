#!/usr/bin/env bash

export masternode=$1
export size=3
export user=admin
export pass=admin
export VERSION='3.1.1'
export cookie='a192aeb9904e6590849337933b000c99'

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
