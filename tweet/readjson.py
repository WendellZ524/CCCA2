import json
import time
import os

Greaterincome = "AurinGreaterIncome.json"
GreaterPopulation = "AurinPopulation.json"
rawGeojson = "rawGeojson.json"

'''
define interesting cities
'''
cities=["Greater Sydney","Greater Melbourne","Greater Adelaide"]


def read_json():
    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = os.path.dirname(current_dir)
    dir = os.path.join(current_dir,"data")
    filename = "pro35.json"
    with open(os.path.join(dir,filename),encoding="utf8") as jf:
        targets = json.load(jf)


    #########################################################
    '''
    compute
    '''
    theme = "income"
    Greater_income_json = convert_json(theme,targets,cities)
    theme = "population"
    Greater_population_json = convert_json(theme,targets,cities)
    theme = "rawGeojson"
    GeoJson = convert_json(theme,targets,cities)
    #print(Greater_income_json[,'features'][0]['properties'])

    ########################################################
    '''
    write result to files
    '''
    write_json("greater_income_goe.json",Greater_income_json)
    write_json("greater_Population_goe.json",Greater_population_json)
    write_json("rawGeojson.json",GeoJson)



def write_json(filename,j_src):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = os.path.dirname(current_dir)
    dir = os.path.join(current_dir,"data")
    path = os.path.join(dir,filename)
    with open(path,"w") as t:
        json.dump(j_src,t)  


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


def load_json(filename):

    current_dir = os.path.dirname(os.path.abspath(__file__))
    current_dir = os.path.dirname(current_dir)
    dir = os.path.join(current_dir,"data")
    if filename == "income":
        filename = Greaterincome
    elif filename == "population":
        filename = GreaterPopulation
    else:
        pass
    try:
        with open(os.path.join(dir,filename),encoding="utf8") as jf:
            res = json.load(jf)
    except :
        print("file {%s} does not exist",filename)
    return res

def convert_json(theme,targets,cities):
    '''
    load json file
    '''
    print("Loading files")
    time_start=time.time()
    source = load_json(theme)
    time_end=time.time()
    print(theme,"Files loaded in %d s",time_end-time_start)
    features = source['features']
    res= targets.copy()
    cps = []
    res['features']=[]
    for i,feature in enumerate(features):
        name = feature['properties']['feature_name']
        points = feature['geometry']['coordinates'][0]
        if theme == "population":
            value = feature['properties']["p_tot"]
        elif theme == "income":
            value = feature['properties']['income_aud']
        else:
            theme = "value"
            value = 0
        #calculate the interested city'central point
        cp = get_cp(points[0])
        
        item = {"type": "Feature",
            "properties":
                {theme:value,
                "id":i,
                "name":name,
                "cp":cp
                },
            "geometry":
                {"type":"Polygon",
                "coordinates":points}}
        # get values
        
        # get interest cities
        if name in cities:
            res['features'].append(item)
            cps.append(cp)
        res['size'] = len(res['features'])
        #calculate the center point of all cities interesed
        res['cp'] = get_cp(cps)


    return res

#read_json()