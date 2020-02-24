'''
@File  : test.py
@Author: Piepis
@Date  : 2020/2/22 15:19
@Desc  : 
'''

from flask import Flask,request,jsonify,abort
import random

app = Flask(__name__)  #实例化一个Flask对象

@app.route("/api/user/reg",methods=['POST'])

def reg():
    if not request.json or "name" not in request.json or "password" not in request.json:
        abort(404)
    res = [
        {
            "code": "100000",
            "msg": "成功",
            "data": {
                "name": "李六",
                "password": "e10adc3949ba59abbe56e057f20f883e"
            }
        },
        {
            "code": "100001",
            "msg": "失败，用户已存在",
            "data": {
                "name": "李六",
                "password": "e10adc3949ba59abbe56e057f20f883e"
            }
        },
        {
            "code": "100002",
            "msg": "失败，添加用户失败",
            "data": {
                "name": "李六",
                "password": "e10adc3949ba59abbe56e057f20f883e"
            }
        }
    ]
    return jsonify(random.choice(res))

if __name__=='__main__':
    pass
    print('Test')