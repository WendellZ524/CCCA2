from keys import *
from utils import *

def twitterCollect(collect_location,location_dict,couch_url,keyword_list,mode):
    db_name=None
    search_location=None
    if collect_location in location_dict.keys():
        print("Collecting tweets from:", collect_location)
        db_name="tweets_test1"
        search_location=[(collect_location,location_dict[collect_location])]
    elif collect_location=="all":
        print("Collecting tweets from all areas")
        db_name="tweets_test1"
        n =[(location,coordinate) for location,coordinate in location_dict.items()]
    else:
        print("The location'",collect_location,"'is not supported")
        print("Please type location from:",list(location_dict.keys()))
        print("System exiting...")
        exit(0)

    search_since = '2021-01-01'
    # bouding box for melbourne
    bounding_box = [140.9773, -39.2363, 146.9429, -34.0006]

    api = get_api(consumer_key, consumer_secret, access_token, access_token_secret)
    db = get_db(couch_url, db_user, db_pw, db_name)

    if mode=="search":
        for location,coordinate in search_location:
            for keyword in keyword_list:
                tweets = cursor_search(api, keyword=keyword, location=coordinate, since=search_since, n=1)
                tweets_to_db(tweets, db, keyword,location)

    elif mode == 'stream':
        for location,coordinate in search_location:
            for keyword in keyword_list:
                # tweets are implicitly added to db in the listener class
                tweets=stream_tweet(api, bounding_box=bounding_box,keyword=keyword,db=db,location=location)

    else:
        print("Wrong search mode")
        print("System exiting...")
        exit(0)


