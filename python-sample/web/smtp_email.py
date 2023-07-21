import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg.set_content("你好，我是测试邮件")

msg["Subject"] = "问候邮件"
msg["From"] = "from@example.com"
msg["To"] = "to@example.com"

# 邮箱支持SSL就用SMTP_SSL，否则用SMTP
s = smtplib.SMTP_SSL("smtp.example.com", 465)
username = "user@example.com"
password = "密码当然是保密的"
s.login(username, password)
s.send_message(msg)
s.quit()
