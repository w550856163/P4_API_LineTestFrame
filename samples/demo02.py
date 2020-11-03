#!/usr/bin/env python
# -*coding: UTF-8 *-
# @File   ：demo02.py
# @Author ：wwd
# @Date   ：2020/10/25 1:24 上午
import logging

logger = logging.getLogger('test_p3p4')
logger.setLevel(logging.DEBUG) #设置日志默认
#创建日志格式对象
con_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_formatter = logging.Formatter('%(asctime)s - %(message)s')

sh = logging.StreamHandler() #创建控制台输出对象
sh.setFormatter( con_formatter )#设置日志格式
sh.setLevel( logging.DEBUG )#设置日志等级

fh = logging.FileHandler('test.log','a',encoding='utf-8')
fh.setFormatter( file_formatter )
fh.setLevel( logging.DEBUG )

logger.addHandler( sh )
logger.addHandler( fh )

logger.info('hello')



