# %%
import os
import shutil
from pathlib import Path

desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")

# copy windows hosts file to desktop folder
shutil.copy(r"C:\Windows\system32\drivers\etc\hosts", rf"{desktop}")

# %%
desktop_hosts = Path(rf"{desktop}\hosts")
with desktop_hosts.open() as f:
    print(f.read())
# %%
desktop_hosts.unlink()

# %%
