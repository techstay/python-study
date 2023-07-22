# %%
import datetime

import pymysql

# docker
"""
docker run --name some-mysql `
    -e MYSQL_ROOT_PASSWORD=123456 `
    -e MYSQL_DATABASE=test `
    -d --rm -p 3306:3306 `
    mysql:latest
"""

host = "localhost"
username = "root"
password = "123456"
db_name = "test"

create_table_sql = """\
CREATE TABLE fuck(
id INT AUTO_INCREMENT PRIMARY KEY,
username VARCHAR(255) UNIQUE ,
nickname VARCHAR(255) NOT NULL ,
birthday DATE
)
"""

insert_table_sql = """\
INSERT INTO fuck(username,nickname,birthday)
 VALUES(%s,%s,%s)
"""

query_table_sql = """\
SELECT id,username,nickname,birthday
FROM fuck
"""

delete_table_sql = """\
DELETE FROM fuck
"""

drop_table_sql = """\
DROP TABLE fuck
"""

connection = pymysql.connect(
    host=host, user=username, password=password, charset="utf8mb4", db=db_name
)

# %%

cursor = connection.cursor()

cursor.execute(create_table_sql)
connection.commit()
# %%

# 插入数据
cursor.execute(insert_table_sql, ("yitian", "易天", datetime.date.today()))
cursor.execute(insert_table_sql, ("zhang3", "张三", datetime.date.today()))
cursor.execute(insert_table_sql, ("li4", "李四", datetime.date.today()))
cursor.execute(insert_table_sql, ("wang5", "王五", datetime.date.today()))
connection.commit()

# %%

cursor.execute(query_table_sql)
results = cursor.fetchall()
print("id\tname\tnickname\tbirthday")
for row in results:
    print(row[0], row[1], row[2], row[3], sep="\t")

# %%
cursor.execute(delete_table_sql)
connection.commit()

# %%
connection.cursor().execute(drop_table_sql)
connection.commit()
connection.close()
