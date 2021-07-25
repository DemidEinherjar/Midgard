import pymongo

client = pymongo.MongoClient("mongodb+srv://user88:Vif3tDH38S1FZF4P@asgard.dsapa.mongodb.net/testData?retryWrites=true&w=majority")
db = client.testData
coll = db.users

#res = coll.count_documents({}) #кол-во всех коллекций (записей в БД)

#res = coll.count_documents({'name': {'$regex': "Odi."}}) #кол-во коллекций по регулярному выражению

#res = client.list_database_names() #кол-во баз данных

#res = db.list_collection_names() #коллекции базы данных testData

#coll.drop() #удаление коллекции

