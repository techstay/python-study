# %%
from tempfile import TemporaryFile

with TemporaryFile() as f:
    f.write(b"Hello World")
    f.seek(0)
    data = f.read()
    print(data)

# %%
