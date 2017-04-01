print('--------------空类型--------------')
print(f'None type:{type(None)}')
print(f'None value:{None}')

print('--------------整数类型--------------')
print(f'Integer type:{type(100)}')
print(f'Integer value:{100}')

# 各种进制
decimal = 100
binary_number = 0b1100
octal_number = 0o12374
hexadecimal = 0xcafe

print(f'八进制:{oct(decimal)}')
print(f'十六进制:{hex(decimal)}')
print(f'二进制:{bin(decimal)}')

# 特别的运算符
result = 5 / 3
print(f'/ 是小数除:{result}')
result = 5 // 3
print(f'// 是整除:{result}')
result = 5 ** 3
print(f'**是乘方:{result}')

print('--------------浮点数类型--------------')
print(f'Float type:{type(3.14)}')
print(f'Float value:{3.14}')

# 各种小数
float_number = 3.1415
exp_number = 0.31415e1
print(f'float:{exp_number}')

print('--------------布尔类型--------------')

print(f'Bool type:{type(True)}')
print(f'Bool value:{False}')

print('--------------复数类型--------------')
complex1 = 1 + 2j
complex2 = 2 + 3j
print('复数类型：', type(complex1))
print('复数：', complex1 + complex2)
print('复数{0}的实部：{1}，虚部是：{2}'.format(complex1, complex1.real, complex1.imag))
print('{0}的共轭复数是：{1}'.format(complex1, complex1.conjugate()))

print('--------------字符串类型--------------')
print(f'String type:{type("")}')
print(f'string value:{"fuck"}')

multiLineString = '''\
这是一个多行字符串
首行的\\表示第一行被忽略
'''
print(multiLineString)

rawString = r"\n不会被转移"
print(f'原始字符串:{rawString}')

formattedString = f"{3.14}"
print(f'格式化字符串:{formattedString}')

print('--------------序列类型的切片操作--------------')
serial = list(range(0, 11))
print(f'前五个元素:{serial[0:5]}')
print(f'后五个元素:{serial[-6:-1]}')
print(f'第4个到最后:{serial[3:]}')
print(f'第2个元素:{serial[1]}')

serial = [1, 2, 3, 4, 5]
serial[2:4] = []
print(f'删除切片 serial={serial}')

print('--------------列表--------------')
print(f'list type:{type([])}')

# 新建列表
list1 = []
list2 = list()

# 插入元素
list1.append(1)
list1.append(2)
list1.extend(range(3, 6))
list1.insert(2, 9)

print(f'插入元素 list1:{list1}')

# 删除元素
list1.remove(5)
del list1[2]
print(f'删除元素 list1:{list1}')

# 清除列表
list1.clear()
print(f'清除列表 list1:{list1}')

# 栈操作
list2.append(1)
list2.append(2)
list2.pop()
print(f'list2:{list2}')

# 列表解析

squareList = []
for i in range(1, 10):
    squareList.append(i ** 2)

print(f'平方列表:{squareList}')

squareList = [i * i for i in range(1, 10)]
print(f'平方列表:{squareList}')

oddList = [i for i in range(1, 10) if i % 2 != 0]
print(f'奇数列表:{oddList}')

complexList = [(x, y) for x in range(1, 5) if x % 2 == 0 for y in range(1, 5) if y % 2 != 0]
print(f'复杂列表:{complexList}')

print('--------------元组--------------')
print(f'tuple type:{type((5,))}')

tuple1 = ()
tuple1 = tuple()
tuple2 = (1, 2, 3, 4, 5)
tuple3 = (50,)
tuple2 = (5, 6)
a, b = tuple2
print(f'a={a},b={b}')

print('--------------集合--------------')
print(f'set type:{type(set())}')

set1 = set()
set2 = {1, 2, 3, 4}

# 添加元素
set1.add(3)
set1.add(4)
set1.add(9)
set1.add(5)
set1.add(4)
print(f'set1 :{set1}')

# 删除元素
set1.remove(4)

# 不可变集合
set1 = frozenset(set1)

# 集合操作
print(f'交:{set1 & set2}')
print(f'并:{set1 | set2}')
print(f'差:{set1 - set2}')
print(f'对称差集:{set1 ^ set2}')

print('--------------字典--------------')
print(f'dict type:{type({})}')

dict1 = {}
dict2 = dict()
dict2 = {1: 2, 2: 4, 3: 6}

dict1[1] = 1
dict1[2] = 2
print(f'dict1:{dict1}')

dict1[2] = 3
print(f'dict1:{dict1}')

del dict1[2]
print(f'dict1:{dict1}')

print(f'dict2.keys:{dict2.keys()}')
print(f'dict2.values{dict2.values()}')

for k, v in dict2.items():
    print(f"[{k}:{v}]", end=' ')
print()

print('--------------序列类型--------------')
longString = 'abcdefghijklnm'

print(f'整个序列:{longString[:]}')
print(f'前5个:{longString[0:5]}')
print(f'后5个:{longString[-6:-1]}')
print(f'前五个之后的所有:{longString[6:]}')
print(f'后五个前面所有的:{longString[:-6]}')
print(f'所有元素:{longString[0:1000]}')

longList = [1, 2, 2, 3, 4, 56, 6, 7, 8, 9, 0]

print(f'longList:{longList}')
longList[0:3] = [5]
print(f'longList:{longList}')

print('--------------列表解析--------------')

cubeList = [i ** 3 for i in range(1, 10)]
print(f'cubeList:{cubeList}')


