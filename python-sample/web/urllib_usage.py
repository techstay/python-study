# %%
from urllib import request

with request.urlopen("https://httpbin.org/ip") as web:
    for line in web:
        print(line.decode("UTF8"), end="")

# %%
proxies = {"https": "https://127.0.0.1:7890"}
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36 Edg/115.0.1901.183"
}
url = "https://httpbin.org/ip"
url2 = "https://google.com"
opener = request.build_opener(request.ProxyHandler(proxies))
request.install_opener(opener)

req = request.Request(url, headers=headers)
response = request.urlopen(req)

print(response.read().decode())

# %%
