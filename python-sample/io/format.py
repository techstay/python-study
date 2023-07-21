# %%
li = [1, 2, 3, 4, 5]
print(str(li))
print(repr(li))

# %%
name = "john"
age = 24
print("{0} is {1} years old".format(name, age))
print("{name} is {age} years old".format(name=name, age=age))

# %%
pi = "3.14"
print(f"rjust():{pi.rjust(7)}")
print(f"ljust():{pi.ljust(7)}")
print(f"zfill():{pi.zfill(7)}")
# %%
import math  # noqa: E402

print("PI is {0:.3f}".format(math.pi))
print("100 is {integer:5d}".format(integer=100))
print(f"PI is {math.pi:.4f}")

# %%
print("hello", "world")
print("hello", "world", sep="|")

# %%
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}x{i}={i * j:<5}", end="")
    print()
# %%
from pprint import pprint  # noqa: E402

d = {"name": "john", "age": 18, "gender": "male"}

pprint(d)

# %%
