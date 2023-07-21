# %%
import subprocess

prog = subprocess.run("ls".split(" "), shell=True, check=True, capture_output=True)

# %%
prog.args
# %%
prog.returncode
# %%
prog.stdout
# %%
