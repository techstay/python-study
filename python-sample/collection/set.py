# %%
s1 = set()
s2 = {1, 2, 3, 4}
immutable_set = frozenset([1, 2, 3, 4])
# %%
s1.add(1)
s1.add(2)
s1.add(5)
s1.add(6)
s1.add(1)

# %%
s1.remove(2)
# %%
s1 | s2
# %%
s1 & s2
# %%
s1 - s2
# %%
s1 ^ s2
# %%
