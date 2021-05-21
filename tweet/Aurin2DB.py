'''
this file is to upload a local json file to DB
the location is ./data/filename.json
xiaofeng zhang
'''


from utils import update_db
from utils import load_json
import argparse
import os
import json
dbname = "aurin_data"

# read Aurin data from local, upload aurin datas to DB
def get_aurin_json(theme):

    if theme == "greater_Population_goe.json":
        myjson = load_json(theme)
        print("try to save aurin data")
        update_db(dbname,"Aurin_pop",myjson)
        print(theme,"uploaded ")

    elif theme == "greater_Income_goe2.json" :
        myjson = load_json(theme)
        id = "Aurin_income"
        print("try to save aurin data")
        update_db(dbname,id,myjson)
        print(theme,"uploaded ")

def main():
    if args.theme =="all":
        get_aurin_json("greater_Income_goe2.json")
        get_aurin_json("greater_Population_goe.json")
    elif args.theme == "income":
        get_aurin_json("greater_Income_goe2.json")
    elif args.theme == "pop":
        get_aurin_json("greater_Population_goe.json")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--theme', help="theme, income or population",default="income")
    parser.add_argument('--target','-t',help="target databst",default="aurin_data")
    args=parser.parse_args()

    main()
    pass
