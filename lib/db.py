'''
@File  : db.py
@Author: Piepis
@Date  : 2020/2/22 11:26
@Desc  : 
'''
import pymysql

class DB(object):
    def __init__(self):
        self.conn = pymysql.connect(host='127.0.0.1',
                                    port = 3306,
                                    user = 'root',
                                    passwd = '123456',
                                    db = 'api_test')
        self.cur = self.conn.cursor()

    def __del__(self):
        self.cur.close()
        self.conn.close()

    def query(self,sql):
        self.cur.execute(sql)
        return self.cur.fetchall()

    def exec(self,sql):
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            print(str(e))

    def check_user(self,username):
        result = self.query("select * from test where username='{}'".format(username))
        return True if result else False

    def del_user(self,username):
        self.exec("delete from test where username='{}'".format(username))

if __name__=='__main__':
    db = DB()
    result = db.check_user('lisi')
    print(result)






