#!/usr/bin/env python
# -*coding: UTF-8 *-
# @File   ：demo03.py
# @Author ：wwd
# @Date   ：2020/10/26 3:35 下午
import logging
import time
from logging import handlers

logger = logging.getLogger('newdream')
logger.setLevel( logging.DEBUG )

formatter = logging.Formatter('%(asctime)s - %(message)s')
th = handlers.TimedRotatingFileHandler("test.log",when='D',interval=1,backupCount=5)
th.setFormatter( formatter )
th.setLevel( logging.DEBUG )
th.suffix = "%Y_%m_%d_%H_%M_%S.log" #设置日志格式名称

logger.addHandler( th )

logger.info('hello1')
time.sleep(4)
logger.warning('hello2')
time.sleep(4)
logger.error('hello3')