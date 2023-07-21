# %%
import random

random.choice(["apple", "banana", "orange"])
# %%
random.random()
# %%
random.randint(1, 10)
# %%
random.randrange(1, 10)
# %%
random.sample(range(100), 10)
# %%
random.uniform(1.5, 4.5)
# %%
li = [x for x in range(20) if x % 2 == 0]

random.shuffle(li)
# %%
