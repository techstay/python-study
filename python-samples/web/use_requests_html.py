from requests_html import HTMLSession
import json
from pprint import pprint
import io

session = HTMLSession()
r = session.get('https://www.qiushibaike.com/text/')
# # 网页文本
# print(r.html.html)
#
# # 获取链接
# print(r.html.links)
# print(r.html.absolute_links)

# # 首页菜单文本
# print(r.html.find('div#menu', first=True).text)
# # 首页菜单元素
# print(r.html.find('div#menu a', first=True))
# # 段子内容
# print(list(map(lambda x: x.text, r.html.find('div.content span'))))

# print(r.html.xpath("//div[@id='menu']", first=True).text)
# print(r.html.xpath("//div[@id='menu']/a"))
# print(r.html.xpath("//div[@class='content']/span/text()"))

# 获取元素
# e = r.html.find("div#hd_logo", first=True)
# print(e.text)
# print(e.attrs)
# print(e.absolute_links)
# print(e.links)
# print(e.html)
# print(e.search("糗事{}科")[0])

# JS渲染
# r = session.get('http://python-requests.org/')
# r.html.render()
# print(r.html.search('Python 2 will retire in only {months} months!')['months'])

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:62.0) Gecko/20100101 Firefox/62.0'
# 自定义UA
# r = session.get('http://httpbin.org/get', headers={'user-agent': ua})
# pprint(json.loads(r.html.html))

# 表单登录
# r = session.post('http://httpbin.org/post', data={'username': 'yitian', 'passwd': 123456})
# pprint(json.loads(r.html.html))

# 简书用户文章列表
# r = session.get('https://www.jianshu.com/u/7753478e1554')
# r.html.render(scrolldown=50, sleep=.2)
# titles = r.html.find('a.title')
# for i, title in enumerate(titles):
#     print(f'{i+1} [{title.text}](https://www.jianshu.com{title.attrs["href"]})')

# 爬取天涯论坛帖子
url = 'http://bbs.tianya.cn/post-culture-488321-1.shtml'
r = session.get(url)
# 楼主名字
author = r.html.find('div.atl-info span a', first=True).text
# 总页数
div = r.html.find('div.atl-pages', first=True)
links = div.find('a')
total_page = 1 if links == [] else int(links[-2].text)
# 标题
title = r.html.find('span.s_title span', first=True).text

with io.open(f'{title}.txt', 'x', encoding='utf-8') as f:
    for i in range(1, total_page + 1):
        s = url.rfind('-')
        r = session.get(url[:s + 1] + str(i) + '.shtml')
        # 从剩下的里面找楼主的帖子
        items = r.html.find(f'div.atl-item[_host={author}]')
        for item in items:
            content: str = item.find('div.bbs-content', first=True).text
            # 去掉回复
            if not content.startswith('@'):
                f.write(content + "\n")
