# %%
import random

N = 1000000
dice = {}

for _ in range(N):
    k = random.randint(1, 6)
    v = dice.get(k, 0)
    dice[k] = v + 1

print(dice)

# %%
