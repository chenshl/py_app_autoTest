#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/22 23:59
# HTMLTestRunner生成html测试报告


from tools.writelog import writelog
import time
from HTMLTestRunner import HTMLTestRunner
import unittest
test_dir = './case'  #测试脚本存放路径
discover = unittest.defaultTestLoader.discover(test_dir,pattern='test_*.py')
writelog('info','=============')
writelog('info','搜寻测试脚本结束')
print("aaa")
if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H-%M-%S')
    filename = './result/html/' + u'APP自动化测试报告_' + now + '.html'  #拼接测试报告完整路径
    fp = open(filename,'wb')
    runner = HTMLTestRunner(stream=fp,
                            title=u'APP自动化测试报告' + now,
                            description=u'''
                            内部接口测试报告结果（仅供参考）,
                            请只查看成功与失败的结果，错误的一般为脚本错误导致执行错误。''')

    writelog('info','开始测试...')
    runner.run(discover)
    writelog('info','测试结束...')
    fp.close()
    writelog('info','保存html报告成功')
    writelog('info', '=============')