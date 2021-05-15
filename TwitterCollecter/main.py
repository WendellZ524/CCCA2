from sys import argv
from collect import twitterCollect
from twint_search import twintCollect

'''the main function to collect tweets using twitter api'''

location_dict={"melbourne":"-37.984361,145.023796,80km","sydney":"-33.805858,150.851091,110km",
               "adelaide":"-34.9578547,138.742948,70km"}

couch_url = 'http://127.0.0.1:8787/'
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






# the keyword list
# commute =["drive to work","drive commute","take bus to work","bus commute","taxi to work","uber to work","taxi commute"]
