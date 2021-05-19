import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["lib"]
books = db["books"]
""" print(
    books.update_one({
        "name":"autobiography of a yogi"
    },{
        "$set":{
           "author":"krishna" 
        }
    }).modified_count
)
"""
books.update_many({"author":"yogi"},{
    "$set":{
        "name":"yogi a life"
    }
})

print([*books.find()])

