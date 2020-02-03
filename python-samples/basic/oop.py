print('--------------类--------------')


class Person:
    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    def __str__(self):
        return f'Person(name:{self.name},age:{self.age})'

    def introduce_myself(self):
        print(f"I'm {self.name}, I'm {self.age} years old.")


yitian = Person('yitian', 24)
yitian.introduce_myself()

zhang3 = Person('zhang3', 25)
print(yitian)
print(f'population:{Person.population}')

print('--------------类继承--------------')


class Student(Person):
    def __init__(self, id, name, age):
        Person.__init__(self, name, age)
        self.id = id

    def __str__(self):
        return f'Student(id:{self.id},name:{self.name},age:{self.age})'

    def introduce_myself(self):
        print(f"I'm {self.name}, I'm {self.age} years old student.")


xiaoming = Student(1, 'xiaoming', 14)
print(xiaoming)
xiaoming.introduce_myself()

# 调用父类版本
Person.introduce_myself(xiaoming)

print('--------------继承关系--------------')

print(f'xiaoming is Student:{isinstance(xiaoming, Student)}')
print(f'xiaoming is Person:{isinstance(xiaoming, Person)}')
print(f'Student is Person:{issubclass(Student, Person)}')
print(f'Person is Student:{issubclass(Person, Student)}')

print('--------------结构体--------------')


class StudentInfo:
    pass


info = StudentInfo()
info.name = 'yitian'
info.age = 24
info.gender = 'male'

print(f'info({info.name},{info.age},{info.gender})')

print('--------------迭代器--------------')

list1 = [1, 2, 3]
iter1 = iter(list1)
e1 = next(iter1)
e2 = next(iter1)
e3 = next(iter1)

print('List:', e1, e2, e3)


class IterableObj:
    def __init__(self, data):
        self.data = data
        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data) - 1:
            raise StopIteration
        self.index += 1
        return self.data[self.index]


print('IterableObj:', end=' ')
obj1 = IterableObj([1, 2, 3])
for i in obj1:
    print(i, end=' ')
print()

print('--------------生成器--------------')


def even_generator(data):
    index = 0
    while index < len(data):
        if data[index] % 2 == 0:
            yield data[index]
        index += 1


integer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f'even_generator:{[i for i in even_generator(integer_list)]}')

print('--------------生成器表达式--------------')

odd_generator = (i for i in range(1, 11) if i % 2 != 0)

odd_list = [i for i in range(1, 11) if i % 2 != 0]

print(f'generator type:{type(odd_generator)}')
print(f'list type:{type(odd_list)}')
