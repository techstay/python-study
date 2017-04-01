print('--------------导入模块--------------')

import sys

print(f'{sys.path}')

print('--------------列出模块名称--------------')
from basic import hello

print(dir(hello))

