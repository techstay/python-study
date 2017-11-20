from  pymongo import MongoClient
from pprint import pprint

# 连接数据库
client = MongoClient('localhost', 27017)

# 选择数据库
db = client['hello']

# 获取集合
user = db.user

# 插入数据
user.insert_one({"_id": 1, "name": "yitian", "age": 24})
user.insert_one({"_id": 2, "name": "zhang3", "age": 25})
user.insert_one({"_id": 3, "name": "li4", "age": 26})

# 更新数据
user.update_one({"_id": 1}, {"$set": {"name": "易天"}})
user.update_many({}, {"$inc": {"age": 1}})

# 查询数据
yitian = user.find_one({"name": "yitian"})
yitian = user.find_one({"_id": 1})
pprint(yitian)

print("------所有数据--------")
for u in user.find():
    pprint(u)

print("------年龄大于25的--------")
for u in user.find({"age": {"$gt": 25}}):
    pprint(u)

# 删除所有数据
user.remove({})
