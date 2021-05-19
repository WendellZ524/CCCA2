# how to use fetchDB.py

args: 

--souce,-s, the souce db name which store the twitters and view

--target,-t, the target db name that store the result json file

--docid, id shown in couchDB, if duplicate, update value.
    
    docid examples:
        if want location and count: --docid loc_count(Default)
        if want location, year, and count: --docid loc_year_count --time 2020
        this will return the result of 2020 and the docid in couchDB will be "loc_year_count_2020"

--time,  definet the year of datas. default is 2021
