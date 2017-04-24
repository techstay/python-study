import logging

'''============日志配置============'''
# 创建Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# 创建Handler

# 终端Handler
consoleHandler = logging.StreamHandler()
consoleHandler.setLevel(logging.INFO)

# 文件Handler
fileHandler = logging.FileHandler('log.log', mode='w', encoding='UTF-8')
fileHandler.setLevel(logging.ERROR)

# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
consoleHandler.setFormatter(formatter)
fileHandler.setFormatter(formatter)

# 添加到Logger中
logger.addHandler(consoleHandler)
logger.addHandler(fileHandler)

import urllib.parse as parse


def get_baidu_url_name(name, encoding='GBK'):
    return parse.quote(name, encoding=encoding)


'''============通用工具============'''
import requests

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
headers = {'User-Agent': user_agent}


def get_url_content(url, method='get', encoding='utf8'):
    m = method.lower()
    html = None
    if m == 'get':
        html = requests.get(url, headers=headers)
    elif m == 'post':
        html = requests.post(url, headers=headers)
    else:
        raise Exception('HTML方法不对')
    html.encoding = encoding
    return html.text
