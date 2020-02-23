'''
@File  : BaseCase.py
@Author: Piepis
@Date  : 2020/2/22 16:48
@Desc  : 
'''

import unittest
import requests
import json
import sys
sys.path.append("../..")
from lib.read_excel import *

class BaseCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        if cls.__name__ != 'BaseCase':
            cls.data_list = excel_to_list(data_file,cls.__name__)

    def get_case_data(self,case_name):
        return get_test_data(self.data_list,case_name)

    def send_request(self,case_data):
        case_name = case_data.get('case_name')
        url = case_data.get('url')
        args = case_data.get('args')
        headers = case_data.get('headers')
        expect_res = case_data.get('expect_res')
        method = case_data.get('method')
        data_type = case_data.get('data_type')

        if method.upper()=='GET': #GET类型请求
            res = requests.get(url=url,params=json.loads(args))

        elif data_type.upper()=='FORM': #表单格式请求
            res = requests.post(url=url,data = json.loads(args),headers = json.loads(headers))
            self.assertEqual(res.text,expect_res)
        else:  #JSON格式请求
            res = requests.post(url=url,json=json.loads(args),headers= json.loads(headers))
            self.assertDictEqual(res.json(),json.loads(expect_res))




