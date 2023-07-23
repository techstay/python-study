# python-study

**注意：之前我的很多代码练习都是分项目存放的，最后搞得很乱，现在整理到了一起，本项目将存档，变为只读状态。如果有后续更新的话，统一放到[我的学习笔记](https://github.com/techstay/studyNotes/tree/main/python)项目里。**

我的 python 学习笔记。

- [python-sample](./python-sample/README.md)，一些 Python 语言的示例
- [thirdparty-libraries](./thirdparty-libraries/README.md)，一些 PPython 第三方类库的示例
- checkio 和[empireofcode](./empireofcode/README.md)，两者的练习题，做了一点就弃坑了
- [scrapy-sample](./scrapy-sample)，scrapy 类库的爬虫示例
- enjoybeautiful，使用爬虫爬取福利图片的代码

还有一些不重要的和没整理完的就不列举了。

## 开发环境

### 安装 python

推荐使用 scoop 安装 python，简单方便。

```powershell
scoop install python
```

然后配置 PyPI 镜像，使用国内镜像可以加快下载速度。

```sh
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
```

### 环境变量

在 powershell 终端中执行以下命令，即可开启 Python UTF8 模式，这样在文件读写的时候就会默认使用 UTF8 编码读写。

```powershell
[Environment]::SetEnvironmentVariable("PYTHONUTF8","1","User")
```

### 包管理器

包管理器用于从 PyPI 安装第三方类库，Python 世界中有很多包管理器可供选择。

- pip，Python 自带的包管理器。它会将所有包安装在全局环境中，所以有可能出现冲突，而且没办法按项目做版本管理。所以诞生了大量的工具来解决这个问题。
- virtualenv，因为官方的 pip 对虚拟环境支持不完善，所以就有了 virtualenv 工具，专门用来创建虚拟环境，配合 pip 就能做到分项目的依赖管理，目前也是常用的一种手段。不过现在我们拥有了一些更加方便的包管理器，可以简化这一过程，所以没必要在手动使用 virtualenv 管理虚拟环境了。
- anaconda，与其说这是一个包管理器，不妨说它是一个完整的 Python 运行环境。使用 Python 进行科学计算、人工智能等领域的项目，需要安装大量相关类库，anaconda 简化了这一过程，它直接帮你把所有用得到的类库打包，可以一次性完整安装，缺点就是 anaconda 的安装包真的很大。除此以外，anaconda 还可以用来管理 Python 版本，可以很方便的创建不同版本的运行环境。
- pipenv，之前我很喜欢使用的一个包管理器。但是这个项目因为作者维护不力，和社区产生了一些矛盾，停更了一段时间。这个包管理器因为开发时间比较早，所以在功能上不如后面的两位完善。
- [poetry](https://python-poetry.org/)，这也是一个非常流行的包管理器，在 github 上有大量 star。
- [pdm](https://pdm.fming.dev/latest/)，一个现代的包管理器。相比于前面这些兄弟，pdm 支持一个实验性的特性 PEP 582，不需要像虚拟环境那样要为每个虚拟环境都安装一遍第三方类库，更加节约存储空间。不过这个提案最后被官方否决了-\_-||。[这里](https://github.com/pdm-project/pdm/blob/main/README_zh.md#%E4%B8%8E%E5%85%B6%E4%BB%96%E5%8C%85%E7%AE%A1%E7%90%86%E5%99%A8%E7%9A%84%E6%AF%94%E8%BE%83)有几个包管理器的对比，我推荐使用 pdm。
- pipx，这是一个 Python 软件的包管理器。前面介绍的那些都是通用的包管理器，可以用来安装第三方类库和 Python 编写的软件。而 pipx 专门用来管理 Python 软件，它会在单独的位置安装 Python 软件，保证软件之间隔离互不干扰，创建环境变量，同时也提供了命令行可以直接更新所有软件包。所以通过 pipx 安装前面这些包管理器，再用这些包管理器去管理具体的依赖，是一个很好的方案。

#### pipx

安装

```sh
py -3 -m pip install --user pipx
py -3 -m pipx ensurepath
```

更新

```sh
python3 -m pip install --user -U pipx
```

使用

```sh
# 安装
pipx install <pkg>
# 列出已安装
pipx list
# 卸载
pipx uninstall <pkg>
# 更新所有软件
pipx upgrade-all
```

#### pdm

使用 pipx 安装

```sh
pipx install pdm
```

配置

```sh
# 使用venv后端
pdm config venv.backend venv
# 开启全局下载缓存，节约存储空间
pdm config install.cache on

```

在当前目录创建新项目

```sh
pdm init
```

管理依赖

```sh
# 安装依赖
pdm add <pkg>
# 安装开发依赖
pdm add -d <pkg>
# 更新所有依赖
pdm update
```

### anaconda

scoop 安装 anaconda，或者也可以直接[下载安装包](https://www.anaconda.com/download)进行安装。

```sh
scoop install anaconda3
```

安装完成之后，就可以打开 anaconda navigator 了。这是一个图形化的程序，可以很方便的使用和配置 anaconda 的各项功能。

使用 anaconda 命令管理 python 环境。

```sh
# 列出所有环境
conda env list
# 创建新环境
conda create -n <name>
# 创建环境时同时指定python版本
conda create -n myenv python=3.9
# 克隆一个环境
conda create --name new --clone old
# 激活新环境
conda activate <name>
```

### IDE

之前我一直很喜欢使用 PyCharm 作为 IDE，不过随着 vscode 的发力和 python 生态环境的完善，现在使用 vscode 配合开源组件的使用体验，已经完全不输于 PyCharm 这样的专业付费 IDE。

vscode 安装扩展：

- python，核心扩展
- pylance，语言服务器
- black formatter，非常流行的代码格式化扩展
- flake8，linter 扩展，帮助分析并指出代码中可能存在的错误
- isort，代码风格扩展，将导入类库排序
- jupyter，一组扩展，在 vscode 中提供 jupyter 笔记本的支持
- ruff，另一个 linter

我的 vsocde 配置文件：

```json
{
  "python.analysis.autoImportCompletions": true,
  "python.analysis.completeFunctionParens": true,
  "python.analysis.downloadStubs": true,
  "python.analysis.inlayHints.callArgumentNames": true,
  "python.analysis.inlayHints.pytestParameters": true,
  "python.analysis.inlayHints.variableTypes": true,
  "python.languageServer": "Pylance",
  "python.linting.banditEnabled": true,
  "python.linting.flake8Enabled": true,
  "python.testing.pytestEnabled": true,
  "python.testing.unittestEnabled": true
}
```

安装完成后，重启 vscode，打开一个 python 文件，应该就能看到效果了。点击右下角的 python 语言服务器的图标，开启类型检查，就能提供和静态语言类似的类型检查功能，更加增强代码的健壮性。

执行代码的话有多种执行方式，第一种就是点击右上角的运行文件的图标，这样会在终端中执行文件，如果喜欢交互式的方式的话，也可以点击运行图标的第三个选项，这样就能在打开 REPL 在其中执行代码，更方便实时查看。第二种是将文件写成交互式笔记本的形式，如下所示。前面 扩展安装好之后，vscode 应该会自动识别这种样式，并按照笔记本的方式渲染，点击每个单元格上的执行按钮即可单独执行单元格的内容，并同时在右边的交互式窗格中显示结果。第三种方式就是直接使用 jupyter 笔记本，安装好 anaconda 的话，在 vscode 中创建`.ipynb`格式的文件，然后选择 anaconda 内核，即可在 vscode 中编辑笔记本。或者也可以在 anaconda 中打开网页端笔记本。

```py
#%%
a = 1

#%%
b = 2
```

## 学习

- 《python 核心编程》，口碑很好的一本 python 书
- [python 官方教程](https://docs.python.org/3/tutorial/index.html)
- [awesome-python](https://github.com/vinta/awesome-python)
