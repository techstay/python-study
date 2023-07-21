# %%
import pickle
from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    gender: str


p = Person("jack", 18, "male")

pickle_str = pickle.dumps(p)

# %%

# deserialization may be unsafe, use with caution!
p2: Person = pickle.loads(pickle_str)

# %%
