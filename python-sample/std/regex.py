# %%
import re

text = "abc bbc abbc ddd"

re.findall(r"\w{3}", text)
# %%

pattern = re.compile(r"\bab\w*\b")
pattern.findall(text)
# %%
text = "总共20条数据 每页5条"
pattern = re.compile(r"总共(?P<total>\d+)条数据\s+每页(?P<per_page>\d+)条")

ma = pattern.match(text)

extract_data = ma.groupdict()

extract_data["total"]
# %%
