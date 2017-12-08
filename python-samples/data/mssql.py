import pyodbc
import datetime
server = 'tcp:localhost'
database = 'test'
username = 'sa'
password = '12345678'

create_table_sql = '''
CREATE TABLE author (
  id       INT IDENTITY PRIMARY KEY,
  name     VARCHAR(30) NOT NULL,
  birthday DATE
)
'''

insert_table_sql = '''
INSERT INTO author(name,birthday)VALUES (?,?)
'''

select_table_sql = '''SELECT * FROM author'''

select_one_sql = '''SELECT * FROM author WHERE name = ?'''

drop_table_sql = '''DROP TABLE author'''

connection = connection = pyodbc.connect(
    'DRIVER={ODBC Driver 13 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)

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
