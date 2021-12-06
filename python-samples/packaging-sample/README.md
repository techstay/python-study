# packaging-sample

使用poetry的简单的项目打包例子。既然有poetry这种好用的工具，为什么还要使用setuptools呢？

## 构建包

```sh
poetry build
```

## 测试和运行

用pytest运行单元测试。

```sh
poetry run pytest
```

运行项目。

```sh
poetry run yitian-packaging-sample
```

## 发布包

先把包放到测试pypi上面看看，没问题了再把包正式发布。首先需要添加testpypi的地址。

```sh
poetry config repositories.testpypi https://test.pypi.org/legacy/
```

然后试着发布。没有账号的话提前注册一个。

```sh
poetry publish -r testpypi --build
```

然后就可以在<https://test.pypi.org/project/packaging-sample/>上面看到自己的测试包了。

下载运行确定没问题以后就可以正式发布了。

```sh
poetry publish
```

## 后续工作

后面的事情就简单了，继续提交代码，等到要发新版本的时候指定一个合适的版本号。

```sh
poetry version minor
```

然后再次运行发布命令。就是这么舒服！

```sh
poetry publish
```
