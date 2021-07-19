import pymongo

client = pymongo.MongoClient("mongodb+srv://user88:Vif3tDH38S1FZF4P@asgard.dsapa.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.test
coll = db.new_users
coll.insert_one({'_id': 1, 'name': 'Alex'})

