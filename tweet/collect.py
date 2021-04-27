from keys import *
from utils import *

couch_url = 'http://127.0.0.1:5984/'
db_name = 'search'

search_keyword = '#covid19' + ' -filter:retweets'
search_location = '-37.813629,144.963058,50km'
search_since = '2021-01-01'

#aus [110.05,-44.48,154.92,-10.03]
#vic [140.9773, -39.2363, 146.9429, -34.0006]
bounding_box = [140.9773, -39.2363, 146.9429, -34.0006]

mode = 'search'

api = get_api(consumer_key, consumer_secret, access_token, access_token_secret)
db = get_db(couch_url, db_user, db_pw, db_name)

if mode == 'search':
    tweets = cursor_search(api, search_keyword, search_location, search_since, n=10)
    tweets_to_db(tweets, db)

elif mode == 'stream':
    stream_tweet(api, bounding_box=bounding_box, db=db)

