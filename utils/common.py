#!/usr/bin/env python
#-- coding: utf-8 --

"""

测试脚本执行结束后，自动触发发送测试报告，自动发送测试报告到已经设置到的邮箱中

"""
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import *


# 定义发送邮件
def send_mail(file_new):
    # ----------跟发件相关的参数------
    smtpserver = SMTPSERVER # 发件服务器
    port = 465  # 端口
    sender = SENDER_ACCOUNT  # 账号
    psw = AUTHORIZATION_CODE  # 密码

    receiver = RECEIVER_LIST  # 多个收件人list对象

    # ----------编辑邮件的内容------
    # 读文件
    with open(file_new, "rb") as fp:
        mail_body = fp.read()

    msg = MIMEMultipart()
    msg["from"] = sender  # 发件人
    msg["to"] = ";".join(receiver)  # 多个收件人list转str
    msg["subject"] = "HRM接口测试"  # 主题

    # 正文
    Body = MIMEText(mail_body, "html", "utf-8")
    msg.attach(Body)

    # 附件
    att = MIMEText(mail_body, "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename="test_report.html"'
    msg.attach(att)

    # ----------发送邮件------
    try:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver)  # 连服务器
        smtp.login(sender, psw)
        print('发送成功！')

    except Exception as e:

        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, psw)  # 登录
    smtp.sendmail(sender, receiver, msg.as_string())  # 发送
    print('发送成功！')
    smtp.quit()  # 关闭
