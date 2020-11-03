#!/usr/bin/env python
# -*coding: UTF-8 *-
# @File   ：log_utils.py
# @Author ：wwd
# @Date   ：2020/10/26 4:19 下午

import os
import  logging
from logging import handlers
from common.config_utils import config

#log_path = os.path.join( os.path.dirname(__file__),'..', 'logs')
log_path = os.path.join( os.path.dirname(__file__),'..', config.LOG_PATH )

class LogUtils:
    def __init__(self,log_path = log_path ):
        self.log_file_name = 'API_TEST_LOG'#API_TEST_LOG随便写
        self.logger = logging.getLogger('API_TEST_LOG')
        self.logger.setLevel( logging.DEBUG )

        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')

        console_handler = logging.StreamHandler() #控制台输出
        console_handler.setFormatter(formatter) #格式
        console_handler.setLevel( logging.DEBUG )#等级

        file_handler = handlers.TimedRotatingFileHandler(os.path.join(log_path,self.log_file_name),
                                                         when='D',interval=1,backupCount=7)#一天生成一次。保留7天
        file_handler.setLevel( logging.DEBUG  )#级别
        file_handler.setFormatter( formatter )#格式

        self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)

        console_handler.close()  # 防止打印日志重复
        file_handler.close()  # 防止打印日志重复

    def get_logger(self):
        return self.logger #返回logger对象

logger = LogUtils().get_logger()

if __name__=='__main__':
    logger.debug('newdream')