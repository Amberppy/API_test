'''
@File  : run.py
@Author: Piepis
@Date  : 2020/2/22 18:55
@Desc  : 
'''

import unittest
from config.config import *
from test.suite.test_suites import *
import time
import pickle,sys
import HTMLTestRunner

def discover():
    return unittest.defaultTestLoader.discover(r'D:\ApiTest\test')

def run(suite):
    print("================================== 测试开始 ==================================")

    with open(report_file,'wb') as f:
        #结果赋予result变量
        result = HTMLTestRunner(stream = f,title = 'API Test',description='测试描述',tester='卡卡').run(suite)

    if result.failures: #保存失败用例序列化文件
        save_failures(result,last_fails_file)

    if send_email_after_run: #是否发送邮件
        send_mail(report_file) #从配置文件中读取
    print("================================== 测试结束 ==================================")

def run_all(): #运行所有用例
    run(discover())

def run_suite(suite_name):  #运行'test/suite/test_suites.py'文件中自定义的TestSuite
    suite = get_suite(suite_name)
    if suite:
        run(suite)

    else:
       print('TestSuite不存在')

def collect():
# 由于使用discover（）组装的TestSuite是按文件夹目录多级嵌套的，
# 我们把所有用例取出，放到一个无嵌套的TestSuite中，方便之后操作
    suite = unittest.TestSuite()
    def _collect(tests):
        if isinstance(tests,unittest.TestSuite):
            if tests.countTestCases()!=0:
                for i in tests:
                    _collect(i)
        else:
            suite.addTests(tests) #如果下级元素是TestCase，则添加到TestSuite中
    _collect(discover())
    return suite

def collect_only():#仅列出所有用例
    t0 = time.time()
    i = 0
    for case in collect():
        i +=1
        print("{}.{}".format(str(i),case.id))
    print("----------------------------------------------------------------------")
    print('Collect {} tests is {: .3f}s'.format(str(i),time.time()-t0))

def makesuite_by_testlist(testlist_file):  #test_list_file配置在config/config.py中
    with open(testlist_file) as f:
        testlist = f.readlines()

    testlist = [i.strip() for i in testlist if not i.startswith('#')]# 去掉每行结尾的"/n"和 #号开头的行

    suite = unittest.TestSuite()
    all_cases = collect() #所有用例
    for case in all_cases: #从所有用例中匹配用例方法名
        if case._testMethodName in testlist:
            suite.addTests(case)
    return suite


def save_failures(result,file): #file为序列化保存的文件名，配置在config/config.py中
    suite = unittest.TestSuite()
    for case_result in result.failures:  #组装TestSuite
        suite.addTest(case_result[0])  #case_result是个元祖，第一个元素是用例对象，后面是失败原因等等

        with open(file,'wb') as f:
            pickle.dump(suite,f)

def rerun_fails(): #失败用例重跑方法
    sys.path.append(test_case_path) #需要将用例路径添加到宝搜索路径中，不然反序列化TestSuite会找不到用例
    with open(last_fails_file,'rb') as f:
        suite = pickle.load(f) #反序列化得到TestSuite
    run(suite)

def main():
    if options.collect_only:
        collect_only()
    elif options.rerun_fails:
        rerun_fails()
    elif options.testlist:
        run(makesuite_by_testlist(testlist_file))
    elif options.testsuite:
        run_suite(options.testsuite)
    elif options.tag:
        pass
    else:
        run_all()









