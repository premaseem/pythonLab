"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""
import os
import pymongo

# configure credentials / db name
db_user = os.environ["MONGO_ATLAS_USER"]
db_pass = os.environ["MONGO_ATLAS_PASSWORD"]
db_name = "sample_mflix"

connection_string = f"mongodb+srv://{db_user}:{db_pass}@sharedcluster.lv3wx.mongodb.net/{db_name}?retryWrites=true&w=majority"

client = pymongo.MongoClient(connection_string)
db = client[db_name]

# create database back directory with db_name
os.makedirs(db_name, exist_ok=True)

# list all tables in database
tables = db.list_collection_names()

# dump all tables in db
for table in tables:
    print("exporting data for table", table )
    data = list(db[table].find())
    # write data in json file
    with open(f"{db.name}/{table}.json","w") as writer:
        writer.write(str(data))

exit(0)