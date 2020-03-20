import configparser

config_filename = 'config.ini'
config_content = r'''
[DEFAULT]
name = 易天
age = 30
gender = male

[young]
name = yitian
age = 25
nickname = ${name}

'''

config = configparser.ConfigParser(
    interpolation=configparser.ExtendedInterpolation())

config.read_string(config_content)
config['old'] = {'name': 'yitian', 'age': '52'}

with open(config_filename, 'w', encoding='utf8') as file:
    config.write(file)

del config

config = configparser.ConfigParser()
config.read(config_filename, encoding='utf8')
for section in config.sections():
    print(f'[{section}]')
    for key in config[section]:
        print(f'{key} = {config[section][key]}')

# 有默认值的时候优先使用默认值，会覆盖fallback的值
print(config['young'].get('gender', 'female'))
# getint等函数返回对应类型的值
print(config['young'].getint('age'))
