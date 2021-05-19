import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["lib"]
books = db["books"]
#
#books.insert_one({
#    "name":"autobiography of a yogi",
#    "author":"yss"
#})

books.insert_many([
    {
        "name":"door to light",
        "author":"yogi"
    },
    {
        "name":"leader",
        "author":"mao"
    },
    {
        "name":"inner engineering",
        "author":"sadguru"
    }
])
