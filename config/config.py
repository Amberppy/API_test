'''
@File  : config.py.py
@Author: Piepis
@Date  : 2020/2/22 16:17
@Desc  : 
'''

import logging
import time,os
from optparse import OptionParser

logging.basicConfig(level=logging.DEBUG, #log level
                    format= '[%(asctime)s] %(levelname)s [%(funcName)s: %(filename)s, %(lineno)d] %(message)s',#log格式
                    datefmt='%Y-%m-%d %H:%M:%S', #日期格式
                    filename='log.txt', #日志输出文件
                    filemode='a') #追加模式

# 命令行选项
parser = OptionParser()
parser.add_option('--collect-only',action='store_true',dest = 'collect_only',help='仅列出所有用例')
parser.add_option('--rerun-fails',action='store_true',dest ='return_fails',help='运行上次失败的用例')
parser.add_option('--testlist',action='store_true',dest='testlist',help='运行test/testlist.txt列表')
parser.add_option('--testsuite',action='store',dest='testsuite',help='运行指定的TestSuite')
parser.add_option('--tag',action='store',dest='tag',help='运行指定tag的用例')

(options,args) = parser.parse_args() #应用选项(使生效)

today = time.strftime('%Y%m%d',time.localtime())
now = time.strftime('%Y%m%d_%H%M%S',time.localtime())

log_file = os.path.join(prj_path,'log', 'log_{}.txt'.format(today))  #更改路径到log目录下
report_file = os.path.join(prj_path,'report','report_{}.html'.format(now)) #更改领导report目录下

#增加send_email()开关
send_email_after_run = False

if __name__=='__main__':
    logging.info('hello')