import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["Address"]
books = db["books"]

query = {
    "name" : "autobiography of a yogi"
}

#print([*books.find({
#    "name":"inner engineering"
#},{
#    "author":"yss"
#}
#)])

#print([
#    *books.find().sort("author")
#])
#to sort in ascending order

#print([
#    *books.find().sort("author", 1)
#])
#to sort in decesnding order

#print([
#    *books.find().sort("author", -1).limit(1) # will only give the first one
#])

