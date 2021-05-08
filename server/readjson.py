import json

with open("data3949169542219719605.json",encoding="utf8") as Aurinf:
    features = json.load(Aurinf)['features']




with open("pro35.json",encoding="utf8") as f:
    targets = json.load(f)


#get center
def get_cp(points):
    x = 0 
    y = 0
    k = 0
    for i,point in enumerate(points):
        x += point[0]
        y += point[1]
        k=i
    cp = [x/(k+1),y/(k+1)]
    return cp

def convert_json(features,targets):
    res= targets.copy()
    cps = []
    res['features']=[]
    for i,feature in enumerate(features):
        name = feature['properties']['feature_name']
        points = feature['geometry']['coordinates'][0]
        cp = get_cp(points[0])
        
        item = {"type": "Feature",
            "properties":
                {"confirmed":0,
                "id":i,
                "name":name,
                "cp":cp,
                "childNum":0},
            "geometry":
                {"type":"Polygon",
                "coordinates":points}}

        cities=["Ballarat","Ballarat - North","Ballarat - South"]
        if name in cities:
            print("//*/*/*")
            res['features'].append(item)
            cps.append(cp)
        res['size'] = len(res['features'])
        res['cp'] = get_cp(cps)


    return res

res = convert_json(features,targets)
print(type(res))

with open("test_goe.json","w") as t:
    json.dump(res,t)  