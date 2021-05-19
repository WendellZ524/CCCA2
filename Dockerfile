FROM python:3.8.10-slim-buster

RUN apt-get update && apt-get install -y git

RUN pip install couchdb tweepy numpy websocket git+https://github.com/twintproject/twint.git@origin/master#egg=twint
WORKDIR /data/CCCA2





