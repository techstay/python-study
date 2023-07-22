# %%
from pprint import pprint

from pymongo import MongoClient

# docker
"""
docker run --name some-mongo `
    -d --rm -p 27017:27017 `
    mongo:latest
"""

# 连接数据库
client = MongoClient("localhost", 27017)

# 选择数据库
db = client["test"]

# 获取集合
coll = db.user

# 插入数据
coll.insert_one({"_id": 1, "name": "jack", "age": 18})
coll.insert_one({"_id": 2, "name": "zhang3", "age": 25})
coll.insert_one({"_id": 3, "name": "li4", "age": 26})
# %%
# 更新数据
coll.update_one({"_id": 1}, {"$set": {"name": "leo"}})
coll.update_many({}, {"$inc": {"age": 1}})
# %%
# 查询数据
usr = coll.find_one({"name": "leo"})
pprint(usr)

# %%
for u in coll.find():
    pprint(u)

# %%
for u in coll.find({"age": {"$gt": 25}}):
    pprint(u)

# %%
# 删除所有数据
coll.delete_many({})

# %%
