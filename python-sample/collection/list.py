# %%
type([])
# %%

l1 = []
l2 = list()
# %%
l1.append(1)
l1.append(2)
l1.extend(range(3, 8))
l1.insert(2, 100)

l1

# %%
l1.remove(100)
del l1[2]

l1

# %%
l1.clear()
l1
# %%
# stack operations
l2.append(1)
l2.append(2)
l2.pop()

# %%
[i for i in range(1, 10 + 1)]
# %%

[2 * i for i in range(0, 10)]

# %%
[i for i in range(0, 10) if i % 3 == 0]
# %%
[(x, y) for x in range(1, 11) for y in range(1, 11) if x + y == 10]

# %%

l3 = list(range(1, 5))

for i in l3:
    print(i, end=" ")
print()

# %%
for i in range(len(l3)):
    print(l3[i], end=" ")
print()
# %%
for index, value in enumerate(l3):
    print(f"index:{index}, value:{value}")
print()

# %%
