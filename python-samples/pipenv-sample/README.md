# pipenv-sample

pipenv的简单示例项目。pipenv是一个python的依赖管理工具，可以方便的创建虚拟环境以及管理依赖。

## 安装

最简单的方式，直接用系统pip安装。

```sh
pip install --user pipenv
```

pipx是一个python程序的包管理器，能以隔离的方式安装python程序。如果你安装了pipx，可以用pipx来安装pipenv，更推荐这种方式。

```sh
pipx install pipenv
```

## 配置

默认情况下pipenv会将虚拟环境集中创建在用户家目录下的一个文件夹。我更喜欢将虚拟环境直接创建在项目文件夹下。要如此配置，需要设置相关环境变量。对于linux用户，直接在自己的shell配置中添加下面一行即可。

```sh
export PIPENV_VENV_IN_PROJECT=1 
```

对于windows用户，在Powershell中执行以下命令。

```powershell
[Environment]::SetEnvironmentVariable("PIPENV_VENV_IN_PROJECT", "1", "User")
```

## 使用

键入`pipenv`获取命令行帮助。
