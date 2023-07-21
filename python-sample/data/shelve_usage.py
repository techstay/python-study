# %%
import shelve
from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    username: str
    password: str
    birthday: date


shelve_file = "shelve_db"
with shelve.open(shelve_file) as s:
    s["foo"] = "bar"

    # shelve can save arbitrary python objects
    s["list"] = [1, 2, "a", "b", "c"]

    s["user"] = User("jack", "123456", date(1990, 1, 1))

    # s.sync()
    # s.close()

# %%

with shelve.open(shelve_file) as s:
    # this operation is slow, use carefully!
    for k in s.keys():
        print(k, s[k], sep="=")
# %%
