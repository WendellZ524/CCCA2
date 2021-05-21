'''
1.Fetch twitters from DB,
2.Calculate the result -> a json with Geo
3.upload json to DB
'''
import os
import json
import sys
import argparse
from fetchDB import  fetch_data

from utils import load_json
from utils import update_db



files = ["rawGeojson.json"]


def main():
    dbname=args.source
    if args.docid == "loc_count":
        result = loc_count(dbname)
        update_db(args.target,args.docid,result)
        for feature in result['features']:
            print(feature['properties']['name'],":",feature['properties']['value'])
            #print(len(feature['geometry']["coordinates"][0]))
    if args.docid == "loc_year_count":
        result = loc_year_count(dbname,args.time)
        update_db(args.target,args.docid+"_"+str(args.time),result)
        for feature in result['features']:
            print(feature['properties']['name'],":",feature['properties']['value'])
            #print(len(feature['geometry']["coordinates"][0]))

    #update_db(args.target,args.docid,result)


# location-count
def loc_count(dbname="tweets"):
    view = "keywordLocationYearCounter"
    level = 3
    datas = fetch_data(dbname,view,level=1)

    jsonname= "rawGeojson.json"
    result = load_json(jsonname)
    for item in datas:
        location = item[0][0]
        value = item[1]
        if location == "sydney":
            result['features'][0]["properties"]['value']=value
        if location == "melbourne":
            result['features'][1]["properties"]['value']=value
        if location == "adelaide":
            result['features'][2]["properties"]['value']=value
    return result

def loc_year_count(dbname="tweets",time=2021):

    view = "locationYearCounter"
    level = 2
    datas = fetch_data(dbname,view,level=2)
    print(datas)

    jsonname= "rawGeojson.json"
    result = load_json(jsonname)
    
    for item in datas:
        location = item[0]['location']
        year = item[0]['year']
        value = item[1]
        if year == str(time):
            if location == "sydney":
                result['features'][0]["properties"]['value']=value
            if location == "melbourne":
                result['features'][1]["properties"]['value']=value
            if location == "adelaide":
                result['features'][2]["properties"]['value']=value
    


    return result
    
print("upload result to database")




if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--docid', help="doc id",default="loc_count")
    parser.add_argument('--source','-s',help="twitter databse",default="tweets")
    parser.add_argument('--target','-t',help="target databst",default="twitter_data")
    parser.add_argument('--time',type=str, default= 2021)
    args=parser.parse_args()


    main()
    