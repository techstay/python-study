# Q1
test1 = 'This is a test of the emergency text system'
with open('test.txt', mode='w') as file:
    file.write(test1)

# Q2
test2 = None
with open('test.txt') as file:
    test2 = file.read()

print(test1 == test2)

# Q3
text = '''\
author,book
J R R tolkien,The Hobbit
LynneTruss,"Eats, Shoots & Leaves"
'''
with open('books.csv', mode='w') as file:
    file.write(text)

# Q4
import csv

with open('books.csv') as file:
    books = csv.DictReader(file)
    for book in books:
        print(book)

# Q5
text = '''\
title,author,year
The Weirdstone of Brisingamen,Alan Garner,1960
Perdido Street Station,China Mieville,200
Thud!,Terry Pratchett,2005
The Spellman Files,Lisa Lutz,2007
Small Gods,Terry Pratchett,1992
'''
with open('books.csv', mode='w') as file:
    file.write(text)

# Q6
import sqlite3

db = sqlite3.connect('books.db')
create_sql = '''\
CREATE TABLE books(
title TEXT,
author TEXT,
year INTEGER
)
'''

cursor = db.cursor()
cursor.execute(create_sql)
db.commit()

# Q7
insert_sql = '''\
INSERT INTO books VALUES(?,?,?)
'''

with open('books.csv') as file:
    books = csv.DictReader(file)
    for book in books:
        cursor.execute(insert_sql, (book['title'], book['author'], book['year']))
        db.commit()

# Q8
sql = '''\
SELECT title FROM books ORDER BY title ASC
'''

for row in cursor.execute(sql):
    print(row)

# Q9
sql = '''\
SELECT * 
FROM books ORDER BY year '''

for row in cursor.execute(sql):
    print(row)

# Q10
import sqlalchemy

connection = sqlalchemy.create_engine('sqlite:///books.db').connect()
sql = 'SELECT title FROM books ORDER BY title ASC'
rows = connection.execute(sql)
for row in rows:
    print(row)

# Q11
import redis

server = redis.Redis()
server.hmset('test', {'count': 1, 'name': 'Fester'})
print(server.hgetall('test'))

# Q12
server.hincrby('test', 'count', 3)
print(server.hget('test', 'count'))
