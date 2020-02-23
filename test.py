'''
@File  : test.py
@Author: Piepis
@Date  : 2020/2/22 15:19
@Desc  : 
'''
import json

str = {"code": "100000","msg": "成功","data": {"name": "范冰冰","password": "e10adc3949ba59abbe56e057f20f883e"}}
str_js=json.dumps(str)
print(str_js)
result = json.loads(str_js, encoding='utf-8')
print(type(result))