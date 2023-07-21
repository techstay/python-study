# %%
d1 = {}
d2 = dict()
d3 = {"name": "jack", "age": 18}

# %%

d1[1] = 1
d1
# %%
del d1[1]
d1

# %%
d3.keys()
# %%
d3.values()
# %%

for k, v in d3.items():
    print(f"key:{k}, value:{v}")
# %%
