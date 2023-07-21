# %%
from pathlib import Path

hosts = Path(r"C:\Windows\System32\drivers\etc\hosts")

# open file, process and then close it
with hosts.open() as f:
    content = f.read()
    print(content)

# %%
import os  # noqa: E402

out = Path(r"text.txt")
with out.open(mode="w+") as o:
    o.write("hello world" + os.linesep)
    o.write("file output finished" + os.linesep)

# %%
out.unlink()
# %%
import glob  # noqa: E402

glob.glob("../**/*.py")
