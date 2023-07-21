# %%
class MyContainer:
    _list = []
    _index = 0

    def __init__(self, list):
        self._list = list

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._list):
            raise StopIteration
        else:
            current = self._index
            self._index += 1
            return self._list[current]


my_con = MyContainer([1, 2, 3, 4])
for i in my_con:
    print(i, end=", ")

print()

# %%
