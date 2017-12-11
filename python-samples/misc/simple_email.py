import smtplib

from email.message import EmailMessage

msg = EmailMessage()
msg.set_content('你好，我是测试邮件')

msg['Subject'] = '问候邮件'
msg['From'] = 'an0474@126.com'
msg['To'] = 'asddf14@hotmail.com'

s = smtplib.SMTP('smtp.126.com', 25)
username = ''
password = ''
s.login(username, password)
s.send_message(msg)
s.quit()
