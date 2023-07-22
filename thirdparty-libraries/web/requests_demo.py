# %%
import json

import requests
import requests.cookies

base_url = "http://httpbin.org/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183"
}

# %%

response = requests.get(f"{base_url}get", headers=headers)
print(response.text)

# %%
params = {"name": "jack", "age": 16, "friends": ["zhang3", "li4"]}

response = requests.get(f"{base_url}get", params=params)
print(response.text)

# %%

data = {"name": "jack", "age": 16, "friends": ["zhang3", "li4"]}
response = requests.post(f"{base_url}post", data=data)
print(response.text)

# %%

data = {"name": "jack", "age": 16, "friends": ["zhang3", "li4"]}
response = requests.post(f"{base_url}post", data=json.dumps(data))
print(response.text)

# %%
response = requests.post(f"{base_url}post", json=data)

print(response.text)

# %%
# 发送文件
file = open(r"C:\Windows\System32\drivers\etc\hosts", mode="rb")

data = {"file": file}

response = requests.post(f"{base_url}post", files=data)
print(response.text)

# %%

# 获取cookies

baidu_url = "https://www.baidu.com"
response = requests.get(baidu_url, headers=headers)
print(response.cookies)

# %%

# 发送cookies

cookies = requests.cookies.RequestsCookieJar()
cookies.set("name", "jack")
cookies.set("age", "18")
response = requests.get(f"{base_url}cookies", cookies=cookies)
print(response.text)

# %%
