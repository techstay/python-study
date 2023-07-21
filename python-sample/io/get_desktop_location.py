# %%
def get_windows_desktop_path():
    """
    return C:\\Windows\\techstay\\Desktop
    """
    import subprocess

    out = subprocess.run(
        "powershell -nop -c [Environment]::GetFolderPath('Desktop')".split(" "),
        capture_output=True,
    )

    if out.returncode == 0:
        return out.stdout.decode().strip()
    else:
        raise SystemError("Failed to get Windows desktop path")


if __name__ == "__main__":
    print(get_windows_desktop_path())
# %%
