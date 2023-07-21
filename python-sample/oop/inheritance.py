# %%


class Animal:
    def __init__(self, name) -> None:
        self.name: str = name

    def __str__(self) -> str:
        return f"Animal({self.name})"

    def __repr__(self) -> str:
        return self.__str__()

    def speak(self):
        print(f"Animal {self.name} speaks")


class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def __str__(self) -> str:
        return f"Cat({self.name})"

    def speak(self):
        print(f"Cat {self.name} meows")


class Dog(Animal):
    def speak(self):
        print(f"Dog {self.name} barks")


animals = []

animals.append(Animal("animal"))
animals.append(Cat("kitty"))
animals.append(Dog("snoopy"))

for a in animals:
    a.speak()

# %%
isinstance(animals[1], Animal)
# %%
issubclass(Cat, Animal)
# %%
