'''
@File  : test_suites.py
@Author: Piepis
@Date  : 2020/2/22 18:50
@Desc  : 
'''

import unittest
import sys
sys.path.append('../..')
from test.test_user_login import TestUserLogin
from test.test_user_reg import TestUserReg

smoke_suite = unittest.TestSuite() #自定义的TestSuite
smoke_suite.addTests([TestUserLogin('test_user_login_normal'),TestUserReg('test_user_reg_normal')])


def get_suite(suite_name):
    a = globals().get(suite_name)
    return a






