# %%
import pathlib

pathlib.Path("~/Desktop").expanduser()
# %%
pathlib.Path("~/..").expanduser().resolve()
# %%
