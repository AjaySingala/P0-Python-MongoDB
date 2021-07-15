from pymongo import MongoClient
import datetime

# Establish connection.
client = MongoClient()
print(client)
db = client.test_database
print(db)

# Init collection object.
posts = db.posts
# print(posts)

# # Create a JSON to insert data.
# post = {
#     "author": "Mike",
#     "text": "My first blog post!",
#     "tags": ["mongodb", "python", "pymongo"],
#     "date": datetime.datetime.utcnow()
# }

# # Insert a single document.
# # Returns an instance of InsertOneResult.
# post_id = posts.insert_one(post).inserted_id
# print(post_id)

# # Verify collection created.
# print(db.list_collection_names())

# # Get a single document.
# # Get the first document from the posts collection.
import pprint
# print(posts.find_one())
# pprint.pprint(posts.find_one())     # .pretty()

# # Get documents matchihg author = 'Mike'.
# pprint.pprint(posts.find_one({"author": "Mike"}))
# # No match for 'Eliot'
# pprint.pprint(posts.find_one({"author": "Eliot"}))

# # Create one more JSON to insert data.
# post = {
#     "author": "Eliot",
#     "text": "My blog post on my day at the beach!",
#     "tags": ["travel"],
#     "date": datetime.datetime.utcnow()
# }
# # Returns an instance of InsertOneResult.
# post_id = posts.insert_one(post).inserted_id

# # Query by ObjectID.
# print(post_id)
# pprint.pprint(posts.find_one({"_id": post_id}))

# # ObjectId is not the same as its string representation.
# # Create another JSON to insert data.
# post = {
#     "author": "Mary",
#     "text": "My blog post on cooking!",
#     "tags": ["cooking"],
#     "date": datetime.datetime.utcnow()
# }
# # Returns an instance of InsertOneResult.
# post_id = posts.insert_one(post).inserted_id
# print(post_id)

# post_id_as_str = str(post_id)
# print(post_id_as_str)
# # No result
# pprint.pprint(posts.find_one({"_id": post_id_as_str}))

# # Bulk Inserts.
# new_posts = [
#     {
#         "author": "Mike",
#         "text": "Another post!",
#         "tags": ["bulk", "insert"],
#         "date": datetime.datetime(2009, 11, 12, 11, 14)
#     },
#     {
#         "author": "Eliot",
#         "title": "MongoDB is fun",
#         "text": "and pretty easy too!",
#         "date": datetime.datetime(2009, 11, 10, 10, 45)
#     }
# ]

# print(new_posts[0])
# print(new_posts[1])
# result = posts.insert_many(new_posts)
# print(result)
# print(result.inserted_ids)

# # Querying for more than one document.
# for post in posts.find():
#     pprint.pprint(post)

# # All documents where author = 'Mike'.
# for post in posts.find({'author': 'Mike'}):
#     pprint.pprint(post)

# # Counting.
# print(posts.count_documents({}))
# print(posts.count_documents({"author": "Mike"}))
# print(posts.count_documents({"author": "Eliot"}))

# # Range Queries.
# # Limit results to posts older than a certain date, 
# # but also sort the results by author.
# d = datetime.datetime(2009, 11, 12, 12)
# print("Default sorting...")
# for post in posts.find({"date": {"$lt": d}}).sort('author'):
#     pprint.pprint(post)

# from pymongo import  ASCENDING, DESCENDING
# print("Sorting with pymongo.ASCENDING...")
# for post in posts.find({"date": {"$lt": d}}).sort([('author', ASCENDING)]):
#     pprint.pprint(post)
# print("Sorting with pymongo.DESCENDING...")
# for post in posts.find({"date": {"$lt": d}}).sort([('author', DESCENDING), ('title', ASCENDING)]):
#     pprint.pprint(post)

# # Indexing.
# # Create a new collection called "profiles".
# db.create_collection("profiles")
# print(db.list_collection_names())

# # Create index on user_id.
# from pymongo import  ASCENDING, DESCENDING

# result = db.profiles.create_index([('user_id', ASCENDING)], unique=True)
# # We have two indexes now: one is the index on _id that MongoDB creates
# # automatically, and the other is the index on user_id we just created.
# print(sorted(list(db.profiles.index_information())))

# # Setup some user profiles.
# user_profiles = [
#     {'user_id': 211, 'name': 'Luke'},
#     {'user_id': 212, 'name': 'Ziltoid'}
# ]
# result = db.profiles.insert_many(user_profiles)
# print(result.inserted_ids)

# # Try inserting a duplicate user_id document.
# new_profile = {'user_id': 213, 'name': 'Drew'}
# duplicate_profile = {'user_id': 212, 'name': 'Tommy'}
# # This is fine.
# result = db.profiles.insert_one(new_profile)
# # This will give an error.
# result = db.profiles.insert_one(duplicate_profile)

# # Delete data
# # Delete single document.
# for profile in db.profiles.find():
#     print(profile)

# result = db.profiles.delete_one({'name': 'Drew'})
# print(result.deleted_count)

# for profile in db.profiles.find():
#     print(profile)

# # Delete multiple documents.
# # First add some documents to test,
# temp_profiles = [
#     {'user_id': 213, 'name': 'Starlord'},
#     {'user_id': 214, 'name': 'Starlord'}
# ]
# result = db.profiles.insert_many(temp_profiles)
# print(result.inserted_ids)
# for profile in db.profiles.find():
#     print(profile)

# result = db.profiles.delete_many({'name': 'Starlord'})
# print(result.deleted_count)

# Update data.
# Use the test_collection.
print(db.list_collection_names())

testcoll = db.test_collection

# # Setup some data.
# test_data = [
#     {'x': 1},
#     {'x': 1},
#     {'x': 1},
#     {'x': 4},
#     {'x': 5},
# ]
# result = testcoll.insert_many(test_data)
# print(result.inserted_ids)
# for d in testcoll.find():
#     print(d)

# #Update one doc.
# for d in testcoll.find():
#     print(d)
# result = testcoll.update({'x': 1}, {'x': 10})
# for d in testcoll.find():
#     print(d)

# # Update one using update_one doc.
# for d in testcoll.find():
#     print(d)
# result = testcoll.update_one({'x': 10}, {'$set': {'x': 8}})
# print("after update_one...")
# for d in testcoll.find():
#     print(d)

# Update single document.
# increment x by 3 and update first doc that has x = 1.
#result = testcoll.update_one({'x': 1}, {'$inc': {'x': 3}})
# print(result.matched_count)
# print(result.modified_count)
# for d in testcoll.find():
#     print(d)

# # Update multiple documents.
# result = testcoll.update_many({'x': 1}, {'$inc': {'x': 3}})
# print(result.matched_count)
# print(result.modified_count)
# for d in testcoll.find():
#     print(d)

# # Replace Data.
# for d in testcoll.find():
#     print(d)

# result = testcoll.replace_one({'x': 5}, {'y': 1})
# print(result.matched_count)
# print(result.modified_count)
# for d in testcoll.find():
#     print(d)

# # Upsert: Update if exists. Insert if doesn't.
# # Set the 3rd param of "replace_one" to True.
# for d in testcoll.find():
#     print(d)
# result = testcoll.replace_one({'a': 3}, {'a': 2}, True)
# print(result.matched_count)
# print(result.modified_count)
# print(result.upserted_id)
# for d in testcoll.find():
#     print(d)

# Limit and Projection
# # Setup some user profiles.
# # user_profiles = [
# #     {'user_id': 213, 'name': 'John'},
# #     {'user_id': 214, 'name': 'Mary'},
# #     {'user_id': 215, 'name': 'Smith'},
# #     {'user_id': 216, 'name': 'Neo'},
# #     {'user_id': 217, 'name': 'Trinity'}
# # ]
# # result = db.profiles.insert_many(user_profiles)

print("all docs...")
for doc in db.profiles.find():
    print(doc)
# # Limit the no. of results returned.
# print("Only 2 docs...")
# for doc in db.profiles.find(limit=2):
#     print(doc)
# # Limit which columns are returned.
# # This will print all columns except the “_id” column.
# print("Do not show _id...")
# for doc in db.profiles.find(projection={'_id': False}):
#     print(doc)

# # This will print only the “_id” column.
# print("Show only _id with no projection data...")
# for doc in db.profiles.find(projection={}):
#     print(doc)
# print("Show only _id...")
# for doc in db.profiles.find(projection={'_id': True}):
#     print(doc)
# # This will not print the “_id” and name columns.
# print("Show only name...")
# for doc in db.profiles.find(projection={'name': True, '_id': False}):
#     print(doc)
# # This will not return only 1 document with the “_id” and name columns.
# print("Show only 1 doc with just the name...")
# for doc in db.profiles.find(projection={'name': True}, limit=1):
#     print(doc)
