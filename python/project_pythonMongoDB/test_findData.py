import pymongo
import datetime

client = pymongo.MongoClient("mongodb+srv://user88:Vif3tDH38S1FZF4P@asgard.dsapa.mongodb.net/testData?retryWrites=true&w=majority")
db = client.testData
coll = db.users

#query = {'name': 'Alex'} #запрос точного параметра

#query = {'name': {'$gt': 'A'}} #$gt - см. документацию

#query = {'name': {'$regex': 'Ein*'}} #$regex - использование регулярных выражений

#for value in coll.find(): #по умолчанию метод find возвращает итератор
#    print(value)

#for value in coll.find(query, {'_id': 0, 'status': 1, 'name': 1}): #передаем только те значения, которые необходимы
#    print(value)

#for value in coll.find().limit(3): #вывод только первых 3х значений
#    print(value)

#for value in coll.find().sort('name', 1): #сортировка по убыванию ( -1 по возрастанию)
#    print(value)

for value in coll.find().sort('_id', -1): #сортировка по убыванию ( -1 по возрастанию)
    print(value)