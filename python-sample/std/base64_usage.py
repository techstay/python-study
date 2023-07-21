# %%
import base64

text = b"hello world"

enc = base64.b64encode(text)
# %%
dec = base64.b64decode(enc)
# %%
