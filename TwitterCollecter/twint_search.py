import json
import twint
from keys import *
from utils import *

def twints_to_db(tweets, db , keyword,location):
    for twt in tweets:
        doc={"keyword":str(keyword),"location":location,"year":"2014","text":str(twt["tweet"])}
        try:
            print("Saving to db.........")
            db[twt["id"]] = doc
        except:
            print("skip: same id")
            pass

def twintCollect(collect_location,location_dict,couch_url,keyword_list):
    db_name = None
    search_location = None

    if collect_location in location_dict.keys():
        print("Collecting tweets from:", collect_location)
        db_name="tweets_test1"
        search_location=[(collect_location,location_dict[collect_location])]
    elif collect_location=="all":
        print("Collecting tweets from all areas")
        db_name="tweets_test1"
        search_location=[(location,coordinate) for location,coordinate in location_dict.items()]
    else:
        print("The location'",collect_location,"'is not supported")
        print("Please type location from:",list(location_dict.keys()))
        print("System exiting...")
        exit(0)

    for location, coordinate in search_location:
        for keyword in keyword_list:
            c = twint.Config()
            c.Search = keyword
            c.Limit = 300
            c.Pandas = True
            c.Since = '2015-01-01'
            c.Until = '2016-01-01'
            c.Geo=coordinate

            twint.run.Search(c)

            df = twint.output.panda.Tweets_df
            tweet_dict = df.to_dict(orient='records')
            tweet_json = json.dumps(tweet_dict)
            tweet_json = json.loads(tweet_json)

            db = get_db(couch_url, db_user, db_pw, db_name)
            twints_to_db(tweet_json,db,keyword,location)
