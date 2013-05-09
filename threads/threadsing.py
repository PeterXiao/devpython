# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
MAIL_CONF_FILE = './mail.conf.py'

class Mail:
    def __init__(self, send_conf='default'):
        mail_conf_file = open(MAIL_CONF_FILE, 'r')
        mail_conf_dict = eval(mail_conf_file.read())
        self.mail_conf = mail_conf_dict[send_conf]
    def create(self, header, body, attachment):
        mail = MIMEMultipart()
        for k in header:
            if k == 'subject':
                mail[k] = Header(header[k], 'utf-8')
            elif k == 'to' and isinstance(header[k], list):
                mail[k] = ','.join(header[k])
            else:
                mail[k] = header[k]
        for k in body:
            if k == 'text':
                body_plain = MIMEText(body['text'], 'plain', 'utf-8')
                mail.attach(body_plain)
            elif k == 'html':
                body_html = MIMEText(body['html'], 'html', 'utf-8')
                mail.attach(body_html)
        if attachment:
            for x in range(len(attachment)):
                try:
                    atta_file = open(attachment[x]['path'], 'rb')
                except Exception, e:
                    continue
                try:
                    atta_file_content = atta_file.read()
                except Exception, e:
                    continue
                atta = MIMEText(atta_file_content, 'base64', 'utf-8')
                atta['Content-Type'] = 'application/octet-stream'
                atta['Content-Disposition'] = 'attachment; filename=' + attachment[x]['name']
                mail.attach(atta)
        mail = mail.as_string()
        return mail
    def send(self, recevier, subject, text='', html='', attachment='', sender=''):
        if not text and not html and not attachment:
            return
        if not sender:
            sender = self.mail_conf['user']
        header = {
            'from' : sender,
            'to' : recevier,
            'subject' : subject
        }
        body = {}
        if text:
            body['text'] = text
        if html:
            body['html'] = html
        mail = self.create(header, body, attachment)
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.mail_conf['smtpserver'])
            smtp.login(self.mail_conf['user'], self.mail_conf['pwd'])
            smtp.sendmail(self.mail_conf['user'], receiver, mail)
            smtp.quit()
            return True
        except Exception, e:
            return False

#测试
sender = '1337991560@qq.com'
receiver = ['1337991560@qq.com', 'xxx@sina.com']
subject = 'Python邮件发送测试'
text = '这是一封测试邮件'
html_file = open('./email.html', 'r')
html = html_file.read()
attr = [
    {'name':'sdf.txt', 'path':'./a.txt'}
]
mail_instant = Mail()
a = mail_instant.send(receiver, subject, text, html, attr, sender)
print a