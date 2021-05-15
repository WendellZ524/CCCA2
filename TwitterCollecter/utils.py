import tweepy
import re
import couchdb
from listener import CustomStreamListener


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
    else:
        print("The input db not exist")
        # ans=input("The input db not exist, do you want to create new one? (y/n)")
        print("Creating new db called:", dbname)
        db = couch_server.create(dbname)
    return db


def cursor_search(api, keyword, location, since, n, until=None, language='en'):
    tweets = tweepy.Cursor(api.search, q=keyword, lang=language,
                           geocode=location, since=since, until=until).items(n)
    return tweets


def tweets_to_db(tweets, db, keyword, location):
    for twt in tweets:
        print("location:", twt.user.location, end=" ")
        print("keyword:", keyword, end=" ")
        print('tweet:', twt.text)
        doc = {"keyword": str(keyword), "location": str(location), "year":"2021","text": str(twt.text)}
        try:
            # each id in each tweet is the id in db
            db[str(twt.id)] = doc
        except:
            print("skip: same id")
            pass


def stream_tweet(api, bounding_box, keyword, db, language='en', listener=CustomStreamListener):
    stream_listener = listener(db)
    stream = tweepy.Stream(api.auth, stream_listener)
    stream.filter(track=keyword, locations=bounding_box, languages=language)
