from requests_html import HTMLSession

session = HTMLSession()

response = session.get('https://pipenv.pypa.io/en/latest/')
info = response.html.xpath(
    "//div[@id='pipenv-python-dev-workflow-for-humans']/h1/text()")[0]
print(info)
