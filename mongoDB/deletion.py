import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["lib"]
books = db["books"]

# books.delete_one({
#     "author":"yogi"
# })

# books.delete_many({
#     #add params
# })
print([*books.find()])


