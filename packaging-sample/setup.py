#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 注意 如果要使用上传功能，需要安装twine包:
#   $ pip install twine

import io
import os
import sys
from shutil import rmtree

from setuptools import find_packages, setup, Command

# 包的元信息
NAME = 'yitian_first_package'
DESCRIPTION = '项目的简短描述，不超过200字符'
URL = 'https://github.com/techstay/python-study'
EMAIL = 'lovery521@gmail.com'
AUTHOR = '易天'
REQUIRES_PYTHON = '>=3.6.0'
VERSION = '0.1.0'
KEYWORDS = 'sample setuptools development'

# 项目依赖，也就是必须安装的包
REQUIRED = [
    'requests-html'
]

# 项目的可选依赖，可以不用安装
EXTRAS = {
    # 'fancy feature': ['django'],
}

# 剩下部分不用怎么管 :)
# ------------------------------------------------
# 除了授权和授权文件标识符!
# 如果你改了License, 记得也相应修改Trove Classifier!

here = os.path.abspath(os.path.dirname(__file__))

# 导入README文件作为项目长描述.
# 注意 这需要README文件存在!
try:
    with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
        long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = DESCRIPTION

# 当前面没指定版本号的时候，将包的 __version__.py 模块加载进来
about = {}
if not VERSION:
    with open(os.path.join(here, NAME, '__version__.py')) as f:
        exec(f.read(), about)
else:
    about['__version__'] = VERSION


class UploadCommand(Command):
    """上传功能支持"""

    description = 'Build and publish the package.'
    user_options = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print('\033[1m{0}\033[0m'.format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status('Removing previous builds…')
            rmtree(os.path.join(here, 'dist'))
        except OSError:
            pass

        self.status('Building Source and Wheel (universal) distribution…')
        os.system('{0} setup.py sdist bdist_wheel --universal'.format(sys.executable))

        self.status('Uploading the package to PyPI via Twine…')
        os.system('twine upload dist/*')

        self.status('Pushing git tags…')
        os.system('git tag v{0}'.format(about['__version__']))
        os.system('git push --tags')

        sys.exit()


# 神奇的操作，一个函数完事
setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    keywords=KEYWORDS,
    # 项目中要包括和要排除的文件，setuptools可以自动搜索__init__.py文件来找到包
    packages=find_packages(exclude=('tests',)),
    # 如果项目中包含任何不在包中的单文件模块，需要添加py_modules让setuptools能找到它们:
    # py_modules=['yitian_first_package'],

    # entry_points={
    #     'console_scripts': ['mycli=mymodule:cli'],
    # },
    install_requires=REQUIRED,
    extras_require=EXTRAS,
    # 老旧的distutils需要手动添加项目中需要的非代码文件，setuptools可以用下面参数自动添加(仅限包目录下)
    include_package_data=True,
    # 如果是包的子目录下，则需要手动添加
    package_data={
        'yitian_first_package': ['static/*.html']
    },
    license='MIT',
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    # $ setup.py publish support.
    cmdclass={
        'upload': UploadCommand,
    },
)
