import pymongo

client = pymongo.MongoClient("mongodb+srv://demid:NXU5U13TyHJwqsOtr@asgard.dsapa.mongodb.net/testData?retryWrites=true&w=majority")
db = client.testData
coll = db.users
coll.insert_one({'_id': 1, 'name': 'Alex'})
