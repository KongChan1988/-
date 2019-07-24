# -*- coding:utf-8 -*-
# Author:D.Gray
import unittest,os,time,HTMLTestRunner
def allTests():
    suitte = unittest.TestLoader().discover(
        start_dir=os.path.dirname(__file__),    #获取当前目录路径
        pattern="test_*.py",                    #通过正则获取所有test开头的py文件
        top_level_dir=None                      #默认None
    )
    return suitte
def run():
    # unittest.TextTestRunner(verbosity=2).run(allTests())  #批量执行所有测试用例
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    file_path = os.path.join(os.path.dirname(__file__),"report","%sHtmlTest.html"%now)
    with open(file_path,"wb") as fe:
        HTMLTestRunner.HTMLTestRunner(
            stream=fe,title="自动化测试报告",description="自动化测试报告详细信息"
        ).run(allTests())
if __name__ == '__main__':
    run()