# 为什么电子邮件默认不显示图片

## 运行项目

首先修改`web.py`中的`send_mail`方法中的一些参数，使用你自己邮件地址来替换它们。

```py
def send_mail(email_to):
    msg = EmailMessage()
    with open('email_template.html', 'r', encoding='utf8') as f:
        msg.set_content(f.read(), subtype='html')
    email_from = ''
    username = ''
    password = ''
    smtp_server = ''
    smtp_port = 465
    msg['Subject'] = f'测试邮件{uuid.uuid4()}'

    msg['From'] = email_from
    msg['To'] = email_to
    s = smtplib.SMTP_SSL(smtp_server, smtp_port)
    s.login(username, password)
    s.send_message(msg)
    s.quit()
```

然后运行`web.py`文件即可启动flask服务器。

```sh
python web.py
```

浏览器访问`http://localhost`，然后输入要发送的电子邮件地址即可。稍后在垃圾邮件中应该就可以看到邮件了，点击显示图片，然后观察flask服务器的日志输出，应该可以看到记录了打开邮件的客户端和IP地址。

因此现在各种电子邮件服务商基本上都屏蔽了邮件中的外链图片和脚本，为的就是保护用户的隐私和安全。
