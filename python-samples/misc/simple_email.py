import smtplib

from email.message import EmailMessage

msg = EmailMessage()
msg.set_content('你好，我是测试邮件')

msg['Subject'] = '问候邮件'
msg['From'] = 'public_robot@yitian253.cn'
msg['To'] = 'public_robot@yitian253.cn'

# 邮箱支持SSL就用SMTP_SSL，否则用SMTP
s = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
username = 'public_robot@yitian253.cn'
password = '密码当然是保密的'
s.login(username, password)
s.send_message(msg)
s.quit()
