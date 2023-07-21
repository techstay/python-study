# %%
from dataclasses import dataclass
from typing import ClassVar


class Person:
    # class variables
    count: ClassVar[int] = 0

    # instance variables annotations
    name: str

    # private fields and methods starts with a underscore _
    _secret: str = "secret"

    # constructors
    def __init__(self, name: str, age: int):
        # instance variables
        self.name = name
        # instance variables can also be annotated in __init__ or other methods
        self.age: int = age
        Person.count += 1

    def __str__(self):
        return f"Person(name:{self.name}, age:{self.age})"

    # instance methods
    def introduce_myself(self):
        print(f"I'm {self.name}, I'm {self.age} years old.")


jack = Person("jack", 24)
jack.introduce_myself()

leo = Person("leo", 25)
print(f"people count: {Person.count}")


# %%
@dataclass
class Employee:
    name: str
    age: int
    salary: float


emp1 = Employee("jack", 24, 3000)
print(emp1)
# %%
