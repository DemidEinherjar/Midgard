import pymongo
import datetime

client = pymongo.MongoClient("mongodb+srv://user88:Vif3tDH38S1FZF4P@asgard.dsapa.mongodb.net/testData?retryWrites=true&w=majority")
db = client.testData
coll = db.users
#coll.insert_one({'_id': 1, 'name': 'Demid'}) #запись в коллецию users
data = [
    {
        "_id": 7,
        "name": 'Alex',
        'time': datetime.datetime.now(),
        'status': False,
        'flags': [6, 7, 8, 9, 10]
    },
    {
        '_id': 8,
        'name': 'Einherjar',
        'time': datetime.datetime.now(),
        'status': True,
        'flags': [11, 12, 13, 14, 15]
    }
]
coll.insert_many(data)
