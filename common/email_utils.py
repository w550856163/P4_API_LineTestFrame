#!/usr/bin/env python
# -*coding: UTF-8 *-
# @File   ：email_utils.py
# @Author ：wwd
# @Date   ：2020/10/26 11:53 下午
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from common.config_utils import config
class EmailUtils:
    def __init__(self,smtp_body,smtp_attch_path=None):#邮件附件默认为空
        self.smtp_server = 'smtp.qq.com'
        self.smtp_port = 25
        self.smtp_sender = '2504636440@qq.com'
        self.smtp_password = 'ujjjvlsfowyieacj'
        self.smtp_receiver = config.SMTP_RECEIVER
        self.smtp_cc =config.SMTP_CC
        self.smtp_subject = 'P3P4接口自动化测试报告'
        self.smtp_body = smtp_body
        self.smtp_attch_path = smtp_attch_path

    def email_message_body(self):    #邮件正文的一个方法
        message = MIMEMultipart()
        message['from'] = self.smtp_sender
        message['to'] = self.smtp_receiver
        message['Cc'] = self.smtp_cc
        message['subject'] = self.smtp_subject
        message.attach( MIMEText(self.smtp_body,'html','utf-8') )
        if self.smtp_attch_path: #如果邮件的路径存在
            attach_file_obj = MIMEText(open(self.smtp_attch_path, 'rb').read(), 'base64', 'utf-8')

            attach_file_obj['Content-Type'] = 'application/octet-stream'
            attach_file_obj.add_header('Content-Disposition', 'atachment',
                                       filename=('gbk', '', os.path.basename(self.smtp_attch_path)))
            message.attach(attach_file_obj)
        return message

    def send_mail(self):  #发邮件
        smtp = smtplib.SMTP()
        smtp.connect(self.smtp_server,self.smtp_port)  #邮件服务器 端口
        smtp.login(self.smtp_sender,self.smtp_password) #发件人、授权码
        #smtp.sendmail( self.smtp_sender,[self.smtp_receiver，self.smtp_cc] ,self.email_message_body().as_stri
        #将接收人和传送人切割
        smtp.sendmail( self.smtp_sender,self.smtp_receiver.split(',')+self.smtp_cc.split(',') ,self.email_message_body().as_string() )

if __name__=='__main__':
    email_u = EmailUtils('test使用','./API_TEST_V2.0.html')
    email_u.send_mail()
