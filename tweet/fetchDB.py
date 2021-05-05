
from utils import get_db



size = comm.get_size()

url = 'http://127.0.0.1:8787'
user = "admin"
pw = "admin"
dbname = 'newdb'

db = get_db(url, user, pw, dbname)


doc = db[str(0)]
doc['id']
print(str(doc['text']))

print(len(db))
