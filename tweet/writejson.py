from fetchDB import  fetch_data
import argparse
import  json
import  os




parser = argparse.ArgumentParser(description="get data from couchDB and write to json")
parser.add_argument("-db","--dbname",help="database name",default="incomedb")
args = parser.parse_args()
if args.dbname:
    print(args.dbname)



dbname = args.dbname
sourcejson = '../data/income_geo.json'
targetjson = '../data/incom_result.json'
with open(sourcejson,encoding="utf8") as f:
    source = json.load(f)


datas = fetch_data(args.dbname)
features=source['features']

ROI = {}
for feature in features:
    name = feature['properties']['name']
    ROI[name] = 0

result = {}
for location,value in datas:
    location = location.split(' ')
    for loc in location:
        if loc in ROI:
            ROI[loc] += value
            result[loc] = ROI[loc]

print(result)

def write_json(source,result):
    res = source.copy()
    cps = []
    res['features']=[]

    for i,feature in enumerate(source['features']):
        name = feature['properties']['name']
        if name in result:
            feature['properties']['confirmed'] = result[name]
            res['features'].append(feature)

    return res
res = write_json(source,result)
print(res)