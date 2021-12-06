import requests_html
import pathlib


def hello_world():
    here = pathlib.Path(__file__).parent.resolve()
    htmlpath = pathlib.Path(here / 'static/index.html')
    htmlfile = htmlpath.read_text(encoding='utf-8')
    html = requests_html.HTML(html=htmlfile)
    return html.find('#hello', first=True).text


def main():
    print(hello_world())
