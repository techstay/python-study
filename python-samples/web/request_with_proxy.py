import urllib.request as request
import requests

proxies = {
    'https': 'https://127.0.0.1:1080'
}
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

print('--------------使用urllib--------------')
google_url = 'https://www.google.com'
opener = request.build_opener(request.ProxyHandler(proxies))
request.install_opener(opener)

req = request.Request(google_url, headers=headers)
response = request.urlopen(req)

print(response.read().decode())

print('--------------使用requests--------------')
response = requests.get(google_url, proxies=proxies)
print(response.text)
