# new in python 3.10

# %%
li = [1, 2]

match li:
    case []:
        print("empty list")
    case [1, _]:
        print("list starts with 1")
    case [1, 3]:
        print("list is [1, 3]")
    case [_, _, _] | [_]:
        print("list length is 1 or 3")
    case _:
        print("default")

# %%
