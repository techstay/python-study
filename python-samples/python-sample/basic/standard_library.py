print('--------------os--------------')

import os

print(f'current dir:{os.curdir}')
print(f'os name:{os.name}')
print(f'os path:{os.environ}')
print(f'os linesep:{os.linesep}')

print('--------------shutil--------------')
import shutil

hosts_file = r'C:\Windows\System32\drivers\etc\hosts'
dest_file = r'D:\Desktop\hosts.txt'

shutil.copy2(hosts_file, dest_file)

with open(dest_file) as f:
    print(f.read())

print('--------------glob--------------')
import glob

source_files = glob.glob('*.py')
print(source_files)

print('--------------sys--------------')
import sys

print(sys.argv)

sys.stderr.write('This is a error\n')

print('--------------re--------------')
import re

long_sentence = '''\
When symlinks is false, if the file pointed by the symlink doesn’t exist, an exception will be added in the list of errors raised in an Error exception at the end of the copy process. You can set the optional ignore_dangling_symlinks flag to true if you want to silence this exception. Notice that this option has no effect on platforms that don’t support os.symlink().
'''

results = re.findall(r'\bf\w+', long_sentence)
print(results)

print('--------------math--------------')
import math

print(f'PI is {math.pi}')
print(f'e is {math.e}')

print('--------------random--------------')
import random

for i in range(1, 6):
    print(random.choice([1, 2, 3, 4, 5]), end=' ')
print()

for i in range(1, 6):
    print(random.randrange(1, 100), end=' ')
print()

for i in range(1, 6):
    print(random.randint(1, 10), end=' ')
print()

for i in range(1, 6):
    print(random.uniform(1, 10), end=' ')
print()

list1 = [1, 2, 3, 4, 5]
random.shuffle(list1)
print(f'打乱之后:{list1}')

print('--------------statistics--------------')
import statistics

data = [1, 2, 3, 4, 5, 6, 7, 4, 5, 6, 2, 3, 4, 4, 4, 4]

print(f'平均数:{statistics.mean(data)}')
print(f'中位数:{statistics.median(data)}')
print(f'方差:{statistics.variance(data)}')
print(f'标准差:{statistics.stdev(data)}')
print(f'众数:{statistics.mode(data)}')

print('--------------urllib.request--------------')
import urllib.request

with urllib.request.urlopen('http://www.baidu.com') as web:
    for line in web:
        print(line.decode('UTF8'), end='')

print('--------------datetime--------------')
import datetime

today = datetime.date.today()

now = datetime.datetime.today()

print(f'today:{today}')
print(f'now:{now}')

my_age = today - datetime.date(1994, 7, 7)
print(f'my age:{my_age.days / 365}')

print('--------------zlib--------------')

import zlib

data = b'aaaaa bbbbbbb cccccc dddddddd'

compressed = zlib.compress(data)
print(f'data length:{len(data)}, compressed length:{len(compressed)}')

print(f'compressed:{str(compressed)}')
data = zlib.decompress(compressed)
print(f'data:{str(data)}')
