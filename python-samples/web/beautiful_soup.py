import bs4
import urllib.request as request
import re

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
headers = {'User-Agent': user_agent}
req = request.Request('http://www.qiushibaike.com/', headers=headers)

page = request.urlopen(req).read().decode('utf-8')

soup = bs4.BeautifulSoup(page, "lxml")

divs = soup.find_all('div', class_='article block untagged mb15')
for div in divs:
    links = div.find_all('a', href=re.compile(r'/article/\d*'), class_='contentHerf')
    for link in links:
        contents = link.span.contents
        contents = [i for i in contents if not isinstance(i, bs4.element.Tag)]
        print(contents)
