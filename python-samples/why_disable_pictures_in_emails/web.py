from flask import Flask, request, render_template, redirect, send_file
import smtplib
from email.message import EmailMessage
import uuid

app = Flask(__name__)


def send_mail(email_to):
    msg = EmailMessage()
    with open('email_template.html', 'r', encoding='utf8') as f:
        msg.set_content(f.read(), subtype='html')
    email_from = ''
    username = ''
    password = ''
    smtp_server = 'smtp.mxhichina.com'
    smtp_port = 465
    msg['Subject'] = f'测试邮件{uuid.uuid4()}'

    msg['From'] = email_from
    msg['To'] = email_to
    s = smtplib.SMTP_SSL(smtp_server, smtp_port)
    s.login(username, password)
    s.send_message(msg)
    s.quit()


def is_valid(email):
    import re
    regex = r'^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'
    return re.search(regex, email)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/image')
def image():
    app.logger.info(f'{request.remote_addr} 访问了图片')
    app.logger.info(request.user_agent)
    return send_file('image.png')


@app.route('/send', methods=['GET', 'POST'])
def send():
    email = request.form['email']
    if is_valid(email):
        send_mail(email)
        return redirect('/sended')
    else:
        return '邮件格式不正确'


@app.route('/sended')
def sended():
    return '邮件已发送'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
