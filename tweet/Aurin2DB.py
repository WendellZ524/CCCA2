from utils import loginDB
from readjson import load_json
import os
import json
dbname = "aurin_db"


def update_db(dbname,id,doc):
    db = loginDB(dbname)
    try:
        print("saving")
        db[id] = doc
        print("saved")
    except Exception as e :
        print("doc already exists try to update data")
        data = db[id]
        data[id] = doc
        db.save(data)
        print("data updated")
        pass

# read Aurin data from local, upload aurin datas to DB
def get_aurin_json():
    theme = "greater_population_goe.json"
    myjson = load_json(theme)
    update_db(dbname,"Aurin_pop",myjson)
    print(theme,"uploaded ")


    theme = "greater_income_goe.json"
    myjson = load_json(theme)
    id = "Aurin_income"
    update_db(dbname,id,myjson)
    print(theme,"uploaded ")

if __name__ == '__main__':
    #get_aurin_json()
    pass
