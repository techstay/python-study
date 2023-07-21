# %%
for i in range(1, 11):
    print(i, end=" ")
    if i == 5:
        break
else:
    print("when no break occurs, the else clause executed")
print()

# %%
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")
print()

# %%
