"""
@Author: Aseem Jain
@profile: https://www.linkedin.com/in/premaseem/

"""
import os
from mongoengine import *
db_user = os.environ["MONGO_ATLAS_USER"]
db_pass = os.environ["MONGO_ATLAS_PASSWORD"]
print(db_user, db_pass)
connection_string = f"mongodb+srv://{db_user}:{db_pass}@sharedcluster.lv3wx.mongodb.net/sample_mflix?retryWrites=true&w=majority"

client = connect(host=connection_string)
print("database names: ", client.list_database_names())

# pick up database
db = client["sample_mflix"]
print("collection names: ", db.list_collection_names())

class Y(DynamicDocument):
    pass

# Movies = db.movies
class Movies(DynamicDocument):
    title = StringField(required=True)
    # meta = {'strict': False}
# Movies("title"="abc").save()
m = Movies()
m.title="abc"
m.cast="zyx"
m.save()
# class Movies(Document):
#     title = StringField(required=True)
#     year = IntField()
#     rated = StringField()
#     directors = StringField()
#     cast = ListField()

# print(Movies.objects)
# Movies
for e in Movies.objects(title="abc"):
    print(e.title)
    # print(e._dynamic_fields)
    # print(e.directors)
    # if hasattr(e,"directors"):
    #     print(e.directors)
# for e in col(imdb_id="tt0088763", rating=8.5)
#     print(e)
