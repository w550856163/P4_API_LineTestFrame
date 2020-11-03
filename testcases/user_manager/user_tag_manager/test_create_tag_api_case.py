import requests
import unittest
from common.config_utils import config
import json
from common import api_info
class TestCreatetagApiCase(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
        self.HOSTS = config.HOSTS
    def tearDown(self) -> None:
        self.session.close()

    def test_create_tag(self):
        self._testMethodName = 'case04'
        self._testMethodDoc = '验证create_tag接口能否成功调用'
        '''
        get_param_dict = {
            "grant_type": "client_credential",
            "appid": "wx55614004f367f8ca",
            "secret": "65515b46dd758dfdb09420bb7db2c67f"
        }
        response = self.session.get(url='https://%s/cgi-bin/token' % self.HOSTS,
                                  params=get_param_dict)'''
        response = api_info.get_access_token_api(self.session,self.HOSTS, 'wx55614004f367f8ca', '65515b46dd758dfdb09420bb7db2c67f')
        token_id = response.json()['access_token']
        post_data = {   "tag" : {     "name" : "南P4"   } }
        token_id = api_info.get_access_token_value(self.session, self.HOSTS)

        ''' str_data=json.dumps(post_data,ensure_ascii=False) #把json数据转化成字符串
        print( str_data)
        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/create?access_token=%s'%token_id,
                                             #json=post_data
                                             data=str_data.encode('utf-8'))'''

        response = api_info.create_user_tag_api(self.session, self.HOSTS, token_id, post_data)
        actual_result = response.json()['tag']['name']
        self.assertEqual(actual_result,'南P4','case04 验证create_tag接口能否成功调用')




    def test_create_tag_false(self):
        self._testMethodName = 'case06'
        self._testMethodDoc = '验证create_tag接口标签名非法和其他标签名重复能否正常处理'
        response = api_info.get_access_token_api(self.session,
                                                 self.HOSTS,
                                                 'wx55614004f367f8ca',
                                                 '65515b46dd758dfdb09420bb7db2c67f')
        token_id = response.json()['access_token']
        post_data = {   "tag" : {     "name" : "？？？"   } }
        str_data=json.dumps(post_data,ensure_ascii=False) #把json数据转化成字符串
        print( str_data)
        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/create?access_token=%s'%token_id,
                                     #json=post_data
                                     data=str_data.encode('utf-8'))
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,45157,'case06 验证create_tag接口标签名非法和其他标签名重复能否正常处理')

    def test_create_tag_long(self):
        self._testMethodName = 'case07'
        self._testMethodDoc = '验证create_tag接口标签名长度超过30个字节能否正常处理'
        response = api_info.get_access_token_api(self.session,
                                                 self.HOSTS,
                                                 'wx55614004f367f8ca',
                                                 '65515b46dd758dfdb09420bb7db2c67f')
        token_id = response.json()['access_token']
        post_data = {   "tag" : {     "name" : "abcd坚持就是胜利希望在前方的路上"   } }
        str_data=json.dumps(post_data,ensure_ascii=False) #把json数据转化成字符串
        print( str_data)
        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/create?access_token=%s'%token_id,
                                     #json=post_data
                                     data=str_data.encode('utf-8'))
        actual_result = response.json()['errcode']
        self.assertEqual(actual_result,45158,'case07 验证create_tag接口标签名长度超过30个字节能否正常处理')


    def test_create_tag_shuzi(self):
        self._testMethodName = 'case08'
        self._testMethodDoc = '验证创建纯数字标签'
        response = api_info.get_access_token_api(self.session,
                                                 self.HOSTS,
                                                 'wx55614004f367f8ca',
                                                 '65515b46dd758dfdb09420bb7db2c67f')
        token_id = response.json()['access_token']
        post_data = {   "tag" : {     "name" : '999'   } }
        str_data=json.dumps(post_data,ensure_ascii=False) #把json数据转化成字符串
        print( str_data)

        response = self.session.post(url='https://api.weixin.qq.com/cgi-bin/tags/create?access_token=%s'%token_id,
                                     data=str_data.encode('utf-8'))
        ''' text = response.text
        print(text)
        jsonobj = json.loads(text)
        toCntPercent = jsonobj['tag']['name']
        actual_result = toCntPercent
        print(toCntPercent)'''
        print(response.json())
        actual_result = response.json()['tag']['name']
        self.assertEqual(actual_result,'999','case08 验证验证创建纯数字标签')
if __name__=='__main__':
    unittest.main(verbosity=2)