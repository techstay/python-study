import sqlite3

db_file = 'test.db'
memory_db_file = ':memory:'

create_table_sql = '''\
CREATE TABLE test(
name VARCHAR(255) PRIMARY KEY ,
value VARCHAR(255) NOT NULL 
)
'''

insert_table_sql = """\
INSERT INTO test VALUES(?,?)  
"""

query_table_sql = """\
SELECT *
FROM test WHERE `name`=?
"""

delete_table_sql = """\
DROP TABLE test
"""

print('--------------sqlite3--------------')
print(f'version:{sqlite3.version}')
print(f'sqlite_version:{sqlite3.sqlite_version}')

with sqlite3.connect(memory_db_file) as connection:
    try:
        cursor = connection.cursor()
        cursor.execute(create_table_sql)

        cursor.execute(insert_table_sql, ('name', 'yitian'))
        cursor.execute(insert_table_sql, ('count', '100'))

        cursor.execute(query_table_sql, ('name',))
        name = cursor.fetchone()
        print(name)
        cursor.execute(query_table_sql, ('count',))
        count = cursor.fetchone()
        print(count)

        cursor.execute(delete_table_sql)

    finally:
        cursor.close()
