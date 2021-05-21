from tweet.twitter2DB import loc_year_count
from tweet.twitter2DB import loc_count
from tweet.utils import update_db
import time
files = ["rawGeojson.json"]

def main():
 
        print("update loc_count")
        update_db("twitter_data","loc_count",loc_count())
        print("update loc_year_count")
        update_db("twitter_data","loc_count",loc_count())
        result = loc_year_count()
        update_db("twitter_data","loc_year_count"+"_"+str(2021),result)

    
if __name__ == '__main__':
    while True:
        main()
        print("update finished, sleeping")
        time.sleep(86400)