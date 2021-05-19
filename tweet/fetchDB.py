from utils import loginDB
import os


def fetch_data(dbname,view,level):

    db = loginDB(dbname)
    print(len(db),"docs found in the database")
    datas = []
    for doc in  db.view('textsearch/'+view,group_level = level):
        key = doc.key
        value = doc.value
        #print(key,value)
        datas.append((key,value))

    return datas

