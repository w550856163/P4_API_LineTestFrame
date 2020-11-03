#!/usr/bin/env python
# -*coding: UTF-8 *-
# @File   ：demo04.py
# @Author ：wwd
# @Date   ：2020/10/26 9:31 下午

from nb_log import LogManager

logger = LogManager('newdream').get_logger_and_add_handlers()

logger.debug('P1')
logger.info('P2')
logger.warning('P3')
logger.error('P4')
logger.critical('P5')
print('hello')