from pymongo import MongoClient

client = MongoClient()

# client = MongoClient(host=['localhost:27017'])
# client = MongoClient(host=['mongodbserver:27017'])
# client = MongoClient(host=['197.24.2.19:27017'])

db = client.test            # use products.

x = db.list_collection_names()  # db.getCollectionNames()
print(x)

for i in range(len(x)):
    c = x[i]
    print(f"Searching for documents in collection {c}")
    d = db.get_collection(c)        # db.nameOfcollection
    for e in d.find({"size": 3}):   # db.nameOfCollection.find(...)
        print(e)

