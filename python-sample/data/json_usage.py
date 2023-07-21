# %%

import json
from pprint import pprint

p = {"name": "jack", "age": 18, "gender": "male", "birthday": "1991-11-12"}
json_string = json.dumps(p)
print(f"string1:{json_string}")

# %%
pprint(json.loads(json_string))
# %%

obj = json.loads('[1,2,3,4,"5"]')
pprint(obj)

# %%
