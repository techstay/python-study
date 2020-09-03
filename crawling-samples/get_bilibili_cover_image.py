from requests_html import HTMLSession

userinfo_url = 'https://space.bilibili.com/72956117/video'
save_folder = r'~/Desktop/images'


def get_total_page():
    session = HTMLSession()
    response = session.get(userinfo_url)
    response.html.render()
    total_page = response.html.find('span.be-pager-total', first=True).text
    return int(total_page[2:-3])


def get_image_urls():
    base_url = 'https://api.bilibili.com/x/space/arc/search?mid=72956117&ps=30&tid=0&pn={0}&keyword=&order=pubdate&jsonp=jsonp'
    session = HTMLSession()
    for i in range(1, get_total_page()+1):
        url = base_url.format(i)
        response = session.get(url)
        for i in response.json()['data']['list']['vlist']:
            yield {'name': i['title'], 'url': 'https:'+i["pic"]}


def remove_unvalid_chars(s):
    for c in r'''"'<>/\|:*?''':
        s = s.replace(c, '')
    return s


def download_images():
    import pathlib
    import requests
    import shutil
    folder = pathlib.Path(save_folder).expanduser()
    if not folder.exists():
        folder.mkdir()
    for i in get_image_urls():
        response = requests.get(i['url'], stream=True)
        filename = remove_unvalid_chars(i["name"])+'.jpg'
        with open(folder/filename, 'wb') as f:
            shutil.copyfileobj(response.raw, f)
        print(f'{i["name"]}.jpg下载完成')


download_images()
