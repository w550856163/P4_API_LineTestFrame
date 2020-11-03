#!/usr/bin/env python
# -*coding: UTF-8 *-
# @File   ：email_demo06.py
# @Author ：wwd
# @Date   ：2020/10/26 11:02 下午

import smtplib #负责发送邮件
import os
from email.mime.text import MIMEText#负责构建邮件正文
from email.mime.multipart import MIMEMultipart

smtp = smtplib.SMTP()  #smtp负责连接邮件服务器
smtp.connect('smtp.qq.com',25)
smtp.login('2504636440@qq.com','ujjjvlsfowyieacj')  #邮箱授权码

msg = MIMEMultipart()
msg['from'] = '2504636440@qq.com'#发件人
msg['to'] = '2504636440@qq.com'#收件人
msg['Cc'] = '94608794@qq.com' #抄送人
msg['subject'] = '测试邮件'''
email_content = 'from p4 test...'
msg.attach( MIMEText(email_content,'html','utf-8') )

attach_file_path = os.path.join( os.path.dirname(__file__),'API_TEST_V2.0.html' )
attach_file_obj = MIMEText(open(attach_file_path,'rb').read(),'base64','utf-8' )

attach_file_obj['Content-Type'] = 'application/octet-stream'
attach_file_obj.add_header('Content-Disposition','atachment',
                           filename=('gbk','',os.path.basename(attach_file_path)))

msg.attach( attach_file_obj )#附件对象

#smtp.sendmail('2504636440@qq.com','2504636440@qq.com',msg.as_string()) #发件人、收件人
smtp.sendmail('2504636440@qq.com',['2504636440@qq.com','94608794@qq.com'],msg.as_string()) #发件人、收件人

smtp.close()