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
from readjson import read_json
from readjson import load_json
from Aurin2DB import update_db



files = ["rawGeojson.json"]
#check files
def check_file():
    
    for filename in files:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        current_dir = os.path.dirname(current_dir)
        dir = os.path.join(current_dir,"data")
        try:
            with open(os.path.join(dir,filename),encoding="utf8") as jf:
                pass
        except FileNotFoundError as ferr:
            read_json()

def main():
    check_file()
    dbname=args.source
    if args.docid == "loc_cout":
        result = loc_count(dbname)
        update_db(args.target,args.docid,result)
    if args.docid == "loc_year_count":
        result = loc_year_count(dbname)
        update_db(args.target,args.docid+"_"+str(args.time),result)
    #update_db(args.target,args.docid,result)


# location-count
def loc_count(dbname):
    view = "keywordLocationYearCounter"
    level = 3
    datas = fetch_data(dbname,view,level=1)

    jsonname= "rawGeojson.json"
    result = load_json(jsonname)
    for item in datas:
        location = item[0][0]
        value = item[1]
        if location == "sydeny":
            result['features'][0]["properties"]['value']=value
        if location == "melbourne":
            result['features'][1]["properties"]['value']=value
        if location == "adelaide":
            result['features'][2]["properties"]['value']=value
    return result

def loc_year_count(dbname):

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
        if year == str(args.time):
            if location == "sydeny":
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
    parser.add_argument('--source','-s',help="twitter databse",default="db_withyear")
    parser.add_argument('--target','-t',help="target databst",default="aurin_db")
    parser.add_argument('--time',type=str, default= 2021)
    args=parser.parse_args()


    main()
    