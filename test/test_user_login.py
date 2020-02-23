'''
@File  : test_user_login.py
@Author: Piepis
@Date  : 2020/2/21 10:04
@Desc  : 
'''
import unittest
import requests
from lib.read_excel import *
import json
from BaseCase import BaseCase

class TestUserLogin(BaseCase):

    def test_user_login_normal(self):
        '''leve1:正常登录'''
        case_data = self.get_case_data('test_user_login_normal')
        self.send_request(case_data)

    def test_user_login_password_wrong(self):
        '''密码错误登录'''
        case_data = self.get_case_data('test_user_login_password_wrong')
        self.send_request(case_data)

if __name__=='__main__':
    unittest.main(verbosity=2)

