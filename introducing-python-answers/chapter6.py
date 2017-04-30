# Q1
class Thing:
    pass


example = Thing()

print(Thing)
print(example)


# Q2
class Thing2:
    letters = 'abc'


print(Thing2.letters)


# Q3
class Thing3:
    def __init__(self):
        self.letters = 'xyz'


thing3 = Thing3()
print(thing3.letters)


# Q4
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number


hydrogen = Element('Hydrogen', 'H', 1)

# Q5
kargs = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}
hydrogen = Element(**kargs)


# Q6
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(f'Name:{self.name}, Symbol:{self.symbol}, Number:{self.number}')


hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.dump()


# Q7
class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f'Name:{self.name}, Symbol:{self.symbol}, Number:{self.number}'


hydrogen = Element('Hydrogen', 'H', 1)
print(hydrogen)


# Q9
class Element:
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name

    @property
    def symbol(self):
        return self.__symbol

    @property
    def number(self):
        return self.__number

    def __str__(self):
        return f'Name:{self.__name}, Symbol:{self.__symbol}, Number:{self.__number}'


# Q9
class Bear:
    def eats(self):
        return 'berries'


class Rabbit:
    def eats(self):
        return 'clover'


class Octothorpe:
    def eats(self):
        return 'campers'


bear = Bear()
rabbit = Rabbit()
octothorpe = Octothorpe()

bear.eats()
rabbit.eats()
octothorpe.eats()


# Q10
class Lasor:
    def does(self):
        return 'disintegrate'


class Claw:
    def does(self):
        return 'crush'


class SmartPhone:
    def does(self):
        return 'ring'


class Robot:
    def __init__(self):
        self.lasor = Lasor()
        self.claw = Claw()
        self.smartPhone = SmartPhone()

    def does(self):
        print(f'{self.lasor.does()} {self.claw.does()} {self.smartPhone.does()}')


robot = Robot()
robot.does()
