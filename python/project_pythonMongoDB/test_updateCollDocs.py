import pymongo
client = pymongo.MongoClient("mongodb+srv://user88:Vif3tDH38S1FZF4P@asgard.dsapa.mongodb.net/testData?retryWrites=true&w=majority")
db = client.testData
coll = db.test

#for i in range(20):
#    coll.insert_one({'_id': i, 'name': f'test{i}'})

#замена одного значения
current = {'name': 'test3'}
new_data = {'$set': {'name': 'new'}}
#coll.update_one(current, new_data)

#замена нескольких значений с исп. рег. выражения
#не обязательно заменять то поле, по которому ищем
#можно найти всех пользователей по полю name
#но заменить у них поле password
current_many = {'name': {'$regex': 'test.'}}
new_data_many = {'$set': {'name': 'new'}}
#coll.update_many(current_many, new_data_many)

#использование модификатора с инкрементом
current_inc = {'_id': 1}
new_data_inc = {'$inc': {'balance': 2200}} #вычитаем из значения поля balance 100
#coll.update_many(current_inc, new_data_inc)

#удаляем значение 1го элемента в array
current_array = {'_id': 1}
new_data_array = {'$pop': {'array': 1}} #по индексу
#coll.update_many(current_array, new_data_array)
new_data_array_a = {'$pull': {'array': 'world'}} #по значению

