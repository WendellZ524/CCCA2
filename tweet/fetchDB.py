
from utils import get_db
import os

cmd = 'curl -X GET http://admin:admin@127.0.0.1:8787/'
d = os.system(cmd)




url = 'http://127.0.0.1:8787'
user = "admin"
pw = "admin"
dbname = 'newdb'

db = get_db(url, user, pw, dbname)


print(len(db),"docs in the database")

for i in len(db):
    doc = db[str(0)]
    doc['id']
    print(str(doc['text']))

