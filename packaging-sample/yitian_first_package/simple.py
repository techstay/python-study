import requests_html
import io


def hello_world():
    return 'Hello Python!'


def fetch_msg():
    with io.open('static/index.html', encoding='utf8') as f:
        file = f.read()
    html = requests_html.HTML(html=file)
    return html.find('#hello', first=True).text
