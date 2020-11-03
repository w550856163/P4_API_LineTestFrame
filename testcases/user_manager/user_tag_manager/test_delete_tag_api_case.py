#!/usr/bin/env python
# -*coding: UTF-8 *-
# @File   ：test_delete_tag_api_case.py
# @Author ：wwd
# @Date   ：2020/10/24 8:40 下午
import requests
import unittest
from common.config_utils import config
from common import api_info
from common import api_info
class TestDeletetagApiCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOSTS = config.HOSTS
    def tearDown(self) -> None:
        self.session.close()

    def test_delete_tag(self):
        self._testMethodName = 'case05'
        self._testMethodDoc = '验证delete_tag接口能否成功调用'
        response = api_info.get_access_token_api(self.session,
                                                 self.HOSTS,
                                                  'wx55614004f367f8ca',
                                                 '65515b46dd758dfdb09420bb7db2c67f')
        token_id = response.json()['access_token']

        post_data = {   "tag":{   "id" : 540   } }
        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/delete?access_token=%s'%token_id,
                                     json=post_data)
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,0,'case05 验证delete_tag接口能否成功调用')


    def test_delete_tag_no(self):
        self._testMethodName = 'case10'
        self._testMethodDoc = '验证delete_tag接口不能修改0/1/2这三个系统默认保留的标签'
        response = api_info.get_access_token_api(self.session,
                                                 self.HOSTS,
                                                  'wx55614004f367f8ca',
                                                 '65515b46dd758dfdb09420bb7db2c67f')
        token_id = response.json()['access_token']
        post_data = {   "tag":{   "id" : 2 } }  #0,1,2
        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/delete?access_token=%s'%token_id,
                                     json=post_data)
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,45058,'case10 验证delete_tag接口不能修改0/1/2这三个系统默认保留的标签')

if __name__=='__main__':
    unittest.main(verbosity=2)