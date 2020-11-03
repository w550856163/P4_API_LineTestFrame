#!/usr/bin/env python
# -*coding: UTF-8 *-
# @File   ：demo01.py
# @Author ：wwd
# @Date   ：2020/10/25 1:24 上午
import logging

logging.basicConfig(level=40,  #logging.info
                    format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    filename='test.log')
logging.debug('-----调试信息[debug]-----')
logging.info('-----有用的信息[info]-----')
logging.warning('-----警告信息[warning]-----')
logging.error('-----错误信息[error]-----')
logging.critical('-----严重错误信息[critical]-----')
# debug info warning error critical
#10     20     30     40     50