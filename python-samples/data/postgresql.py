import psycopg2
import datetime

host = 'localhost'
username = 'postgres'
password = '12345678'
db_name = 'test'

create_table_sql = '''
CREATE TABLE author (
  id       SERIAL PRIMARY KEY,
  name     VARCHAR(30) NOT NULL,
  birthday DATE
)
'''

insert_table_sql = '''
INSERT INTO author(name,birthday)VALUES (%s,%s)
'''

select_table_sql = '''SELECT * FROM author'''

select_one_sql = '''SELECT * FROM author WHERE name = %s'''

drop_table_sql = '''DROP TABLE author'''

connection = psycopg2.connect(host=host, user=username, password=password, dbname=db_name)
# 设置自动提交
connection.autocommit = True
try:
    with connection.cursor() as cursor:

        print('--------------新建表--------------')
        cursor.execute(create_table_sql)

        print('--------------插入数据--------------')
        cursor.execute(insert_table_sql, ('易天', '1994-05-06'))
        cursor.execute(insert_table_sql, ('张三', '1995-06-06'))
        cursor.execute(insert_table_sql, ('李四', '1993-11-06'))
        cursor.execute(insert_table_sql, ('王五', datetime.date.today()))

        print('--------------显示数据--------------')
        cursor.execute(select_table_sql)
        results = cursor.fetchall()
        print(f'id\tname\tbirthday')
        for row in results:
            print(row[0], row[1], row[2], sep='\t')

        print('--------------查询数据--------------')
        cursor.execute(select_one_sql, ('易天',))
        results = cursor.fetchall()
        print(f'id\tname\tbirthday')
        for row in results:
            print(row[0], row[1], row[2], sep='\t')

finally:
    cursor = connection.cursor()
    cursor.execute(drop_table_sql)
    cursor.close()
    connection.close()
