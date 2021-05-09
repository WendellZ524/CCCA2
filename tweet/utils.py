import tweepy
import re
import couchdb
import json
import os
from listener import CustomStreamListener
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from shapely.geometry.multipolygon import MultiPolygon


def get_api(consumer_key, consumer_secret, access_token, access_token_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api


def get_db(url, user, pw, dbname):
    server = 'http://' + user + ':' + pw + '@' + re.sub('http://', '', url)
    couch_server = couchdb.Server(server)
    if dbname in couch_server:
        db = couch_server[dbname]
        return db
    else:
        #db = couch_server.create(dbname)
        print(dbname,"does not exist")
        quit()



def cursor_search(api, keyword, location, since, n, until=None, language='en'):
    tweets = tweepy.Cursor(api.search, q=keyword, lang=language,
                           geocode=location, since=since, until=until).items(n)
    return tweets


def tweets_to_db(tweets, db):
    for twt in tweets:
        tweet = twt._json
        print('tweet:', twt.text)
        try:
            db[tweet['id_str']] = tweet
        except:
            pass


def stream_tweet(api, bounding_box, db, language=['en'], keyword=None, listener=CustomStreamListener):
    stream_listener = listener(db)
    stream = tweepy.Stream(api.auth, stream_listener)
    stream.filter(track=keyword, locations=bounding_box, languages=language)


def get_city_name(coord, filepath='../data/income_geo.json'):
    with open(filepath, 'r', encoding='utf8') as f:
        grid_info = json.load(f)
    names = []
    polys = []
    features = grid_info['features']
    for feature in features:
        name = feature['properties']['name']
        poly = Polygon(feature['geometry']['coordinates'][0])
        names.append(name)
        polys.append(poly)
    point = Point(coord)

    for n, p in zip(names, polys):
        if p.intersects(point):
            return n



print(get_city_name((133.88362, -23.69748)))