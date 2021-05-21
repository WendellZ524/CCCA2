from utils import update_db
from readjson import load_json

import os
import json
dbname = "aurin_data"



# read Aurin data from local, upload aurin datas to DB
def get_aurin_json(theme):

    if theme == "greater_population_goe.json":
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

if __name__ == '__main__':
    get_aurin_json("greater_Population_goe.json")
    get_aurin_json("greater_Income_goe2.json")
    pass
