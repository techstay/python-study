import shutil
from pathlib import Path

import requests
from requests_html import HTMLSession, user_agent

# 水蜜桃妹妹，一样是一个早就凉凉的网站
url = "https://smtmm.win/article/52735/"

folder = Path(r"~/Desktop/smtmm/").expanduser()
if not folder.exists():
    folder.mkdir()

session = HTMLSession()
r = session.get(url, headers={"User-Agent": user_agent()})
image_urls = r.html.xpath('//article[@class="article-content"]//img/@data-original')
for image_url in image_urls:
    image = requests.get("https://smtmm.win" + image_url, stream=True)
    filename = image_url[image_url.rfind("/") + 1 :]
    with open(folder / filename, "wb") as f:
        shutil.copyfileobj(image.raw, f)
    print(f"{filename}下载完成")
