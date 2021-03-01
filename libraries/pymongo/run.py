"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""
import pymongo

mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

print("Show Dbs",mongo_client.list_database_names())
my_db = mongo_client["mydatabase"]
my_col = my_db["customers"]
my_dict = {
    "name" : " prem aseem",
    "type" : "gold customer"
}
# _id = my_col.insert_one(my_dict)
# print(_id)

print(my_col.find_one())
print(my_col.count_documents({}))

my_records = [
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
    { "name": "Viola", "address": "Sideway 1633"}
]

# my_col.insert_many(my_records)
# my_col.insert_one({ "_id": 2, "name": "sony", "address": "Highway 37"})
print(list(my_col.find({"name": {"$regex": "^s"}}).sort("name",-1)))
print(list(my_col.find().sort("name",-1)))
# for x in my_col.find({},{ "name": 1, "address": 0 }):
#     print(x)

my_col.update_one({"name":"Sony"},{ "$set" :{"address": "7 cloud heaven"}})
my_col.find_one({"name":"Sony"})
