from requests_html import HTMLSession

session = HTMLSession()

response = session.get('https://html.python-requests.org/')
info = response.html.xpath("//div[@id='requests-html-html-parsing-for-humans-writing-python-3']/h1/text()")[0]
print(info)
