# thirdparty-libraries

一些第三方 Python 类库的例子。

数据库的例子需要对应的数据库，最方便的应该就是用 docker 运行。多行 docker 命令可以使用`\`反斜杠分隔，在 powershell 中则需要使用另一个字符。

```sh
# linux shell
docker run --name some-postgres \
    -e POSTGRES_PASSWORD=123456 \
    -e POSTGRES_DB=test \
    -d --rm postgres
```

```powershell
# powershell
docker run --name some-postgres `
    -e POSTGRES_PASSWORD=123456 `
    -e POSTGRES_DB=test `
    -d --rm postgres
```
