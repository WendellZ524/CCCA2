FROM python:3.8.10-slim-buster
# Add souce dest
ADD ./tweet /server/src
ADD ./data /server/data

RUN pip install couchdb tweepy listener numpy websocket

WORKDIR /server


