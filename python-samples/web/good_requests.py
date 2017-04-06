import requests

base_url = 'http://httpbin.org/'

print('--------------基本使用--------------')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
}

response = requests.get(f'{base_url}get', headers=headers)
print(response.text)

print('--------------附加URL参数--------------')
params = {
    'name': 'yitian',
    'age': 22,
    'friends': ['zhang3', 'li4']
}

response = requests.get(f'{base_url}get', params=params)
print(response.url)

print('--------------POST表单发送数据--------------')
data = {
    'name': 'yitian',
    'age': 22,
    'friends': ['zhang3', 'li4']
}
response = requests.post(f'{base_url}post', data=data)
print(response.text)

print('--------------POST直接发送数据--------------')
import json

data = {
    'name': 'yitian',
    'age': 22,
    'friends': ['zhang3', 'li4']
}
response = requests.post(f'{base_url}post', data=json.dumps(data))
print(response.text)

response = requests.post(f'{base_url}post', json=data)

print('--------------发送文件--------------')
file = open(r'c:\Windows\System32\drivers\etc\hosts', mode='rb')

data = {
    'file': file
}

response = requests.post(f'{base_url}post', files=data)
print(response.text)

print('--------------获取cookies--------------')

baidu_url = "https://www.baidu.com"
response = requests.get(baidu_url)
print(response.cookies)

print('--------------发送cookies--------------')
import requests.cookies

cookies = requests.cookies.RequestsCookieJar()
cookies.set('name', 'yitian')
response = requests.get(f'{base_url}cookies', cookies=cookies)
print(response.text)
