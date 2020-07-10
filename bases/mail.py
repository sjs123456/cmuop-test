#发送邮件的外部库
import smtplib
from email.header import Header
from email.mime.text import MIMEText

def send_email(targetEmail):
    """
    发送邮件
    :param targetEmail:
    :return:
    """

    # 打开测试报告结果
    # r:read
    # b:binary

    f = open("reports\\test_result.html", "rb")

    # 将测试结果放到邮件的主体中
    mail_body = f.read()
    # 关闭测试结果的文件
    f.close()

    # 声明一个邮件对象，用刚刚得到的邮件主体
    msg = MIMEText(mail_body, "html", "utf-8")
    # 设置邮件的主题
    msg["subject"] = Header("Selenium自动化测试结果", "utf-8")
    # 创建一个SMTP服务对象
    # simple message transfer protocol
    # 简单的消息转移协议
    smtpMail = smtplib.SMTP()

    # 连接SMTP的服务器
    # smtp.163.com
    smtpMail.connect("smtp.21cn.com")
    emailFrom = "selenium2@21cn.com"
    password = "Welcome123"
    # 登录SMTP的服务器
    smtpMail.login(emailFrom, password)

    # 使用SMTP的服务器发送邮件
    smtpMail.sendmail(emailFrom, targetEmail, msg.as_string())

    # 退出SMTP对象
    smtpMail.quit()