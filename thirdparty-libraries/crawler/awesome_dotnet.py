import re
from pprint import pprint

import requests_html

# 这个脚本会从awesome-dotnet中抓取所有项目，然后找出其中star数最多的20个
GITHUB_TOKEN = ""

session = requests_html.HTMLSession()
html = session.get(
    "https://raw.githubusercontent.com/quozd/awesome-dotnet/master/README.md"
).html.text
contents = html.split("* [Resources](#resources)")[1]

pattern = re.compile(r"\* \[(\S*)\]\((\S*)\)")
links = pattern.finditer(contents)
data = dict()
with open("awesome-dotnet.txt", "w", encoding="utf8") as output:
    for link in links:
        url: str = link[2]
        if url.startswith("https://github.com/"):
            try:
                repo_name = url.split("https://github.com/")[1].split("/")[1]
                query_url = (
                    "https://api.github.com/repos/"
                    + url.split("https://github.com/")[1]
                )
                repo_info = session.get(
                    query_url,
                    headers={
                        "accept": "application/vnd.github+json",
                        "Authorization": f"Bearer {GITHUB_TOKEN}",
                    },
                ).json()
                count = repo_info["stargazers_count"]
                data[(repo_name, link[2])] = count
                print(f"Repo:{repo_name}, Stars: {count}")
                output.write(f"Repo: {repo_name} , Url: {link[2]} , Stars: {count}\n")
            except (IndexError, KeyError):
                # ignore
                continue

result = [
    (k, data[k])
    for k in sorted(
        data,
        key=data.__getitem__,
        reverse=True,
    )
]
pprint(result[:20])
