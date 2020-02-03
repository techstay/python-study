print('--------------str函数--------------')

a_list = [1, 2, 3, 4, 5]
print(f'str():{str(a_list)}')

print('--------------repr函数--------------')
print(f'repr():{repr(a_list)}')

print('--------------字符串格式化--------------')

name = 'yitian'
age = 24
sentence = '{0} is {1} years old'.format(name, age)
print(sentence)

sentence = '{name} is {age} years old'.format(name=name, age=age)
print(sentence)

print('--------------数字格式化--------------')

pi = '3.14'
print(f'rjust():{pi.rjust(7)}')
print(f'ljust():{pi.ljust(7)}')
print(f'zfill():{pi.zfill(7)}')

import math

print('PI is {0:.3f}'.format(math.pi))
print('100 is {integer:5d}'.format(integer=100))

print('--------------格式化字符串--------------')
print(f'PI is {math.pi:.4f}')

print('--------------终端输入--------------')
# input_string = input('请输入一些语句:')
# print(input_string)

print('--------------终端输出--------------')

print('这是一段输出', '下一段输出', sep=',', end='\n')

print('--------------九九乘法表--------------')
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{j}X{i}={i * j:<5}', end='')
    print()

print('--------------open内置函数--------------')

hosts_file = open(r'C:\Windows\System32\drivers\etc\hosts')

hosts_content = hosts_file.read()
print(hosts_content)

hosts_file.close()

import os

with open('test.txt', 'w') as output:
    output.write('# This is a test file' + os.linesep)
    output.writelines(hosts_content)

print('--------------json--------------')

import json

string1 = json.dumps([1, 2, 3, 'fuck'])
print(f'string1:{string1}')

personal_info = {'name': 'yitian', 'age': 24, 'gender': 'male'}
string2 = json.dumps(personal_info)
print(f'string2:{string2}')

json1 = json.loads('[1,2,3,4,"5"]')
print(f'json1:{json1}')
json2 = json.loads('[{"name":"yitian","age":24},{"name":"zhang3","age":25}]')
print(f'json2:{json2}')
