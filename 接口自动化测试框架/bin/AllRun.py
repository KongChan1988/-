# _*_ coding:utf-8 _*_
# Author:D.Gray
import HTMLTestRunner,os,unittest
import smtplib
from email.mime.text import MIMEText
from time import strftime
from config.Setting import *

class AllRun(object):

    def __init__(self):
        self.report = Report_Path
        self.tests = Tests_Path

    def Suitte(self):
        '''获取所有test开头的文件'''
        self.suitte = unittest.TestLoader().discover(
            start_dir=self.tests,
            pattern="test_*.py",
            top_level_dir=None
        )
        return self.suitte

    def send_mail(self, to_user, sub, content):
        '''
        发送邮件内容
        :param to_user:发送给谁
        :param sub:主题
        :param content:邮件内容
        '''
        global send_mail
        global send_user
        send_mail = 'smtp.163.com'              #邮箱必须开启smtp服务，授权码是密码部分
        send_user = 'wangwei_198811@163.com'    #发邮件的人
        message = MIMEText(content, _subtype='html', _charset='utf-8')      #以HTML格式发送测试报告
        message['Subject'] = sub
        message['From'] = send_user
        message['To'] = to_user
        server = smtplib.SMTP()
        server.connect(send_mail)
        server.login('wangwei_198811@163.com', 'root1988')  #root1988是邮箱授权码
        server.sendmail(send_user, to_user, message.as_string())
        server.close()

    def Report(self):
        '''读取最新测试报告'''
        fireList = os.listdir(self.report)
        file = os.path.join(self.report,fireList[-1])
        with open(file,"rb") as f:
            data = f.read()
            return data

    def Run(self):
        '''主执行逻辑函数'''
        Now = strftime("%Y_%m_%d %H_%M_%S")
        file_path = os.path.join(self.report,"%sReport.html"%Now)       #生产最新测试报告文件
        with open(file_path,"wb") as f:
            HTMLTestRunner.HTMLTestRunner(
                stream=f,title="接口自动化测试报告",description="自动化测试报告"
            ).run(self.Suitte())        #写入测试报告
        self.send_mail(to_user="165022393@qq.com",sub="接口自动化测试报告",content=self.Report())

if __name__ == '__main__':
    run = AllRun()
    run.Run()


