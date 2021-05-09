
from utils import get_db
import os


def fetch_data(dbname):

    #cmd = 'curl -X GET http://admin:admin@127.0.0.1:5984/'
    
    #cmd = 'curl -X GET http://admin:admin@127.0.0.1:8787/'
    #d = os.system(cmd)

    user = "admin"
    pw = "admin"
    try:
        url = 'http://127.0.0.1:5984'
        db = get_db(url, user, pw, dbname)
    except :
        print("access from local machine")
        url = 'http://127.0.0.1:8787'
        db = get_db(url, user, pw, dbname)
    print(len(db),"docs in the database")
    datas = []
    if dbname == 'incomedb':
        for doc in  db.view('textsearch/locationCounter',warpper='location',group=True):
            locatoin = doc.key['location']
            value = doc.value
            #print(locatoin,value)
            datas.append((locatoin,value))
    return datas


