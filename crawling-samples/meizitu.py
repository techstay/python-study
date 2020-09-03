from requests_html import HTMLSession, user_agent
import requests

ua = user_agent()
base_url = 'https://www.mzitu.com/'


def meizitu(url):
    session = HTMLSession()
    r = session.get(url, headers={'user-agent': ua, 'referer': base_url})
    title = r.html.xpath('//h2[@class="main-title"][1]/text()')
    page_url = r.html.xpath('//div[@class="main-image"]//img/@src[1]')

