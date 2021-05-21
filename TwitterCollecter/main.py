from sys import argv
from twitter_search import twitterCollect
from twint_search import twintCollect
import time

'''the main function to collect tweets using twitter api'''
def main():
    location_dict={"melbourne":"-37.984361,145.023796,80km","sydney":"-33.805858,150.851091,110km",
                   "adelaide":"-34.9578547,138.742948,70km"}

    couch_url = 'http://45.113.235.27:5984/'
    # keyword list
    income = ["Mercedes", "Gucci", "Rolex", "LOUIS VUITTON", "yacht", "BMW", "Prada", "Rolls Royce"]

    search_tool=None
    collect_location=None
    search_mode="search" #default
    # type the location in the terminal, or type all to collect all 3 areas
    try:
        search_tool=argv[1].lower()
        collect_location=argv[2].lower()
        search_mode=argv[3].lower()
    except:
        print("Wrong data format")
        print("The first parameter should be the collect method---'twint' or 'twitter'")
        print("The second parameter should be the location name---",location_dict.keys())
        print("The third parameter should be the search mode---'search' or 'stream'")
        exit(1)

    # for the first parameter
    if search_tool=="twitter":
        print("Initiating twitter api collection....")
        twitterCollect(collect_location,location_dict,couch_url,income,search_mode)
    elif search_tool=="twint":
        print("Initiating twint api collection....")
        twintCollect(collect_location,location_dict,couch_url,income)
    else:
        print("The first parameter should be the collect method---'twint' or 'twitter'")
        print("The second parameter should be the location name---",location_dict.keys())
        print("The third parameter should be the search mode---'search' or 'stream'")
        print("-"*100)
        print("Wrong collection method")
        print("Use 'twint' or 'twitter' to collect")

if __name__ == '__main__':
    while True:
        main()
        print("System now is sleeping")
        # run the program once a day
        time.sleep(86400)
