'''
@File  : test_user_reg.py
@Author: Piepis
@Date  : 2020/2/22 11:23
@Desc  : 
'''
import unittest
import requests
from lib.db import DB
from lib.read_excel import *
import json

class TestUserReg(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.data_list = excel_to_list('test_user_data.xlsx','TestUserReg')
        cls.db = DB()

    def test_user_reg_normal(self):
        case_data = get_test_data(self.data_list,'test_user_reg_normal')
        if not case_data:
            print('用例数据不存在')
        url = case_data.get('url')
        data = json.loads(case_data.get('data'))
        expect_res = case_data.get('expect_res')
        expect_res = json.loads(expect_res,encoding='utf-8')
        name = data.get('name')

        #环境检查
        if self.db.check_user(name):
            self.db.del_user(name)
        #发送请求
        res = requests.post(url=url,json=data)
        print(res.text)
        #响应断言（整体断言）
        self.assertEqual(res.text,expect_res)
        #数据库断言
        self.assertTrue(self.db.check_user(name))
        #环境清理（由于注册接口向数据库写入了用户信息）
        self.db.del_user(name)

if __name__=='__main__':
    unittest.main(verbosity=2)