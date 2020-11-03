#!/usr/bin/env python
# -*coding: UTF-8 *-
# @File   ：api_info.py
# @Author ：wwd
# @Date   ：2020/10/24 8:41 下午
import requests
import json
from common.log_utils import logger
from requests.exceptions import ReadTimeout, ConnectionError, RequestException

# def get_access_token_api(session,hosts,**params)
def get_access_token_api(session,hosts,appid,secret,grant_type='client_credential'):
    logger.info('调用获取access_token接口')
    get_param_dict = {
        "grant_type": grant_type,
        "appid": appid,
        "secret": secret
    }
    response = None
    try:
        response = session.get( url='https://%s/cgi-bin/token'%hosts,
                             params=get_param_dict)
    except RequestException as e:
        logger.error('调用获取access_token接口失败，原因是%s'%e.__str__()) #e表示对象，把文档字符串打印出来
    return response


def get_access_token_value(session,hosts): # 登录时候处理关联用的
    response = get_access_token_api(session,hosts,'wx55614004f367f8ca','65515b46dd758dfdb09420bb7db2c67f')
    return response.json()['access_token']
'''
def create_user_tag_api(session,hosts,token_id,post_data):
   # logger.info('调用create_user_tag接口')
    str_data = json.dumps(post_data, ensure_ascii=False)
    response = session.post(url='https://%s/cgi-bin/tags/create?access_token=%s' % (hosts,token_id),
                                 data=str_data.encode('utf-8')
                                 )
    return response'''

def create_user_tag_api(session,hosts,token_id,post_data):
    # logger.info('调用create_user_tag接口')
    str_data = json.dumps(post_data, ensure_ascii=False)
    response = None
    try:
        response = session.post(url='https://%s/cgi-bin/tags/create?access_token=%s' % (hosts, token_id),
                            data=str_data.encode('utf-8'))
    except RequestException as e:
        logger.error('调调用create_user_tag接口失败，原因是%s' % e.__str__())  # e表示对象，把文档字符串打印出来
    return response
