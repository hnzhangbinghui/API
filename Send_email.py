# 参看URL:https://blog.csdn.net/weixin_41522164/article/details/82919571

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
def send_Email():
    smtp_server = 'smtp.163.com'  # 发送邮箱服务器
    port=25 #设置发送服务器的端口号，这里有SSL和TSL两种形式
    from_addr = 'hnzhangbinghui@163.com'  # 发送邮箱
    receiver =[ '809665385@qq.com','15239687008@139.com']  # 接受邮箱,同时发送给多人
    passwd = 'LLCRLRBWGFOMSUKM'  # 发送邮箱密码
    msg = MIMEText('SMTP测试邮件', 'plain', 'utf-8')  # 编写text的类型的邮箱正文
    msg['Subject'] = Header('API_test_html', charset='utf-8')
    msg['from'] = from_addr
    msg['to'] =','.join(receiver)  #逗号分割多个邮箱

    smtpobj = smtplib.SMTP(host=smtp_server, port=25)  # 生成SMTP邮箱对象
    print(type(smtpobj))  # 查看邮箱对象类型
    smtpobj.login(user=from_addr, password=passwd)  # 登陆邮箱
    smtpobj.sendmail(msg['from'],msg['to'].split(','),msg.as_string())  # 发送邮件
    print("发送邮箱成功")

send_Email()