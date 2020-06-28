import re

print(f'{"-" * 20}模式对象{"-" * 20}')
text = 'fuck shit it make she forest'

results = re.findall(r'\b[Ff]\w+', text)
print(results)

pattern = re.compile(r'\b[Ff]\w+')
print(pattern.findall(text))

print(pattern.pattern)
print(pattern.groups)
print(pattern.flags)

print(f'{"-" * 20}search{"-" * 20}')
print(pattern.search(text))

print(f'{"-" * 20}match{"-" * 20}')
result = pattern.match(text)
print(result)

print(f'{"-" * 20}fullmatch{"-" * 20}')
result = pattern.fullmatch(text)
print(result)

result = pattern.fullmatch('fuck')
print(result)

print(f'{"-" * 20}split{"-" * 20}')
print(pattern.split(text))

print(f'{"-" * 20}findall{"-" * 20}')
print(pattern.findall(text))

print(f'{"-" * 20}finditer{"-" * 20}')
print(pattern.finditer(text))

print(f'{"-" * 20}sub{"-" * 20}')
result = pattern.sub("fffffuck", text)
print(result)

print(f'{"-" * 20}subn{"-" * 20}')
t = pattern.subn('ffffuck', text)
print(t)

print(f'{"-" * 20}匹配对象{"-" * 20}')
text = '总共20条数据 每页5条'
pattern = re.compile(r'总共(?P<total>\d+)条数据\s+每页(?P<per>\d+)条')

match = pattern.match(text)
print(match.group(1))

print(match.groups())

print(match.groupdict())
