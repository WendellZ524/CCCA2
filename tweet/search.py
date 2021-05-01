import json
import twint
from keys import *
from utils import *


couch_url = 'http://127.0.0.1:5984/'
db_name = 'twint'
db = get_db(couch_url, db_user, db_pw, db_name)

c = twint.Config()
c.Search = 'data science'
c.Limit = 10
#c.Store_json = True
#c.Output = "tweets.json"
c.Pandas = True
#c.Near = 'melbourne'
c.Geo = '-37.813629,144.963058,50km'
c.Since = '2017-01-01'
c.Until = '2017-12-31'


twint.run.Search(c)
df = twint.output.panda.Tweets_df
print(df)

tweet_dict = df.to_dict(orient='records')
tweet_json = json.dumps(tweet_dict)
tweet_json = json.loads(tweet_json)
for tweet in tweet_json:
    try:
        db[tweet['id']] = tweet
    except:
        pass



