
from utils import get_db
import os

cmd = 'curl -X GET http://admin:admin@127.0.0.1:5984/'
d = os.system(cmd)




url = 'http://127.0.0.1:5984'
user = "admin"
pw = "admin"
dbname = 'newdb'

db = get_db(url, user, pw, dbname)


print(len(db),"docs in the database")

for i in range( len(db)):
    doc = db[str(i)]
    doc['id']
    print(str(doc['text']))
    print("*"*20)

def fetch_data(dbname):
    db = get_db(url, user, pw, dbname)
    doc 