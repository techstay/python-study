# %%
import zlib

data = b"abcdefg xyz"

comp = zlib.compress(data)
# %%

decomp = zlib.decompress(comp)
# %%
