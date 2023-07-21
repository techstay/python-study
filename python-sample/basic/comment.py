#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

# 第一行是shebang，指定linux下Python解释器的路径

# 第二行是文件格式编码

# single line comments

print("comments will not be executed")


def foo():
    """here are document strings

    more detailed contents.
    """
    pass


print(foo.__doc__)
