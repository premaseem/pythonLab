"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""
import os
import pymongo
import json
# configure credentials / db name
db_user = os.environ["MONGO_ATLAS_USER"]
db_pass = os.environ["MONGO_ATLAS_PASSWORD"]
db_name = "sample_mflix"

connection_string = f"mongodb+srv://{db_user}:{db_pass}@sharedcluster.lv3wx.mongodb.net/{db_name}?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_string)
db = client["nflix1"]

with open(f"{db_name}/users.json","w") as reader:
    data = json.load(reader)
print(data)

db.test.insert_many(data)