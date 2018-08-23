import os
import sys
import time
import unittest

curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from util.BaseUtil import BaseUtil
from runner.HTMLTestRunner import HTMLTestRunner

test_suits = unittest.TestSuite()
test_dir = BaseUtil().get_root_path() + '/testcase/'
discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)
for test_case in discover:
    test_suits.addTests(test_case)

if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = BaseUtil().get_root_path() + '/report/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='接口自动化测试结果',
                            description='测试环境')
    runner.run(test_suits)
    fp.close()
