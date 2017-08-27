from typing import TypeVar, Iterable, Tuple, Dict, List

# 变量注解
a: int = 5
b: bool = True
f: float = 5.0
s: str = "abc"
m: Dict[int, int] = {1: 1, 2: 2}
t: Tuple[int, ...] = (1, 2, 3)
l: List[int] = [1, 2, 3, 4]


class MyClass:
    def fun1(self):
        print("fun1")


me: MyClass = MyClass()
me.fun1()


# 函数注解
def add(a: int, b: int) -> int:
    return a + b


help(add)
print(add.__annotations__)
