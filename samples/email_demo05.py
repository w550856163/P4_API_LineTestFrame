#!/usr/bin/env python
# -*coding: UTF-8 *-
# @File   ：email_demo05.py
# @Author ：wwd
# @Date   ：2020/10/26 10:36 下午
import smtplib #负责发送邮件
from email.mime.text import MIMEText#负责构建邮件正文

smtp = smtplib.SMTP()  #smtp负责连接邮件服务器
smtp.connect('smtp.qq.com',25)
smtp.login('2504636440@qq.com','ujjjvlsfowyieacj')  #邮箱授权码

email_content = 'from p4 test...'
msg = MIMEText(email_content,'html','utf-8')
msg['from'] = '2504636440@qq.com'#发件人
msg['to'] = '2504636440@qq.com'#收件人
msg['Cc'] = '329999897@qq.com' #抄送人
msg['subject'] = '测试邮件'''

#smtp.sendmail('2504636440@qq.com','2504636440@qq.com',msg.as_string()) #发件人、收件人
smtp.sendmail('2504636440@qq.com',['2504636440@qq.com','329999897@qq.com'],msg.as_string()) #发件人、收件人

smtp.close()