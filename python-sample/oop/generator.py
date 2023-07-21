# %%
def int_generator():
    for i in range(10):
        yield i + 1


for i in int_generator():
    print(i, end=", ")

print()
# %%

# generator expressions
sum(i for i in range(100 + 1))
# %%
