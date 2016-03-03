from pymongo import MongoClient
from bson.objectid import ObjectId

list = [
ObjectId("1113c4dbbaf03031d620a43e"),
ObjectId("53005ea6baf03031d620a556")
]

prodList = []
stagList = []

client = MongoClient('10.10.160.231', 27017)
db = client['local']
db.authenticate('log_user','logUser3456')

oplog = db['oplog.$main']

for obj in list :
    count = oplog.count({"o._id":obj}).count()
    print count ,
    if(count>0): stagList.append(obj)
    else : prodList.append(obj)

print "Staging object list "
print stagList

print "Production object list"
print prodList

