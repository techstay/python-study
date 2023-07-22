import shutil
from pathlib import Path

import requests
from requests_html import HTMLSession, user_agent

# 这个网站似乎没办法用网页端访问了，也改成了用APP割韭菜，甚是可惜
ua = user_agent()
base_url = "https://www.mzitu.com/"
folder = Path(r"~/Desktop/图片").expanduser()
if not folder.exists():
    folder.mkdir()


def save_image(url, filename, headers):
    img = requests.get(url, stream=True, headers=headers)
    with open(filename, "wb") as f:
        shutil.copyfileobj(img.raw, f)
    print(f"{filename}下载完成")


def meizitu(url):
    session = HTMLSession()
    r = session.get(url, headers={"User-Agent": ua, "Referer": base_url})
    referer = url
    total_page = int(r.html.xpath('//div[@class="pagenavi"]/a/span/text()')[-2])
    title = r.html.xpath('//h2[@class="main-title"][1]/text()', first=True)
    save_folder = folder / title
    if not save_folder.exists():
        save_folder.mkdir()
    for i in range(1, total_page + 1):
        r = session.get(url + f"/{i}", headers={"User-Agent": ua, "Referer": referer})
        image_url = r.html.xpath('//div[@class="main-image"]//img/@src[1]', first=True)
        save_image(
            image_url,
            save_folder / f"{i}.jpg",
            headers={"User-Agent": ua, "Referer": referer},
        )
        referer = url + f"/{i}"


meizitu("https://www.mzitu.com/241840")
meizitu("https://www.mzitu.com/245521")
meizitu("https://www.mzitu.com/24666")
