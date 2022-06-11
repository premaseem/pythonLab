"""
Link: https://www.w3schools.com/python/python_mongodb_create_db.asp

"""

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

mycol = mydb["customers"]


mydict = {
    "name": "John",
    "address": "Highway 37"
}

mylist = [
    { "name": "Amy", "address": "Apple st 652"},
    { "name": "Hannah", "address": "Mountain 21"},
    { "name": "Michael", "address": "Valley 345"},
    { "name": "Sandy", "address": "Ocean blvd 2"},
    { "name": "Betty", "address": "Green Grass 1"},
    { "name": "Richard", "address": "Sky st 331"},
    { "name": "Susan", "address": "One way 98"},
    { "name": "Vicky", "address": "Yellow Garden 2"},
    { "name": "Ben", "address": "Park Lane 38"},
    { "name": "William", "address": "Central st 954"},
    { "name": "Chuck", "address": "Main Road 989"},
    { "name": "Viola", "address": "Sideway 1633"},
    { "name": "Aseem", "address": "Sideway 1633" , "age": 16}
]
# x = mycol.insert(mylist)

# print(x)

# without projection
# x = mycol.find_one({ "name": "Aseem" } )

myquery = { "address": "Valley 345" }
newvalues = { "$set": { "address": "Canyon 123" } }

mycol.update(myquery, newvalues)

# with projection
# result_set = mycol.find({ "age": { "$lt": 18 }   } , { "name":1 , "address": 1  , "_id":0})
result_set = mycol.find().sort("name", 1)
for rec in result_set:
    print(rec)

