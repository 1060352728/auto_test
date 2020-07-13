#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:likui
# https://www.cnblogs.com/qingchengzi/p/7213823.html

import os
import time
import unittest
from email.header import Header
from email.mime.text import MIMEText
from smtplib import SMTP

from HTMLTestRunner import HTMLTestRunner


# 定义发送邮件

def send_mail(file_new):
    '''发送邮件'''

    SMTP_host = 'smtp.126.com'
    # 发信邮箱账号
    username = 'test_tx@126.com'
    # 发信密码一定要126开启smtp发给的密码，不是126登录的密码
    password = 'xxxxxxxxxxxxx'
    # 收件邮箱
    to_address = 'xxxxoooo@qq.com'
    # 邮件标题
    subject = 'UI自动化测试报告'
    # 连接SMTP服务器,此处用126的SMTP服务器
    email_client = SMTP(SMTP_host)
    # 用户名和密码登录
    email_client.login(username, password)

    f = open(file_new, 'rb')
    read = f.read()
    f.close()

    msg = MIMEText(read, _subtype='hmtl', _charset='utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # 邮件主题
    msg['From'] = username  # 定义发送邮件人邮箱
    msg['To'] = to_address  # 定义收邮件人邮箱
    email_client.sendmail(username, to_address, msg.as_string(msg))  # 第一个参数发送人邮箱，第二个参数为收件人邮箱，第三个为发送内容
    email_client.quit()  # 退出


def send_report(testreport):
    '''生成报告'''
    result_dir = testreport
    lists = os.listdir(result_dir)  # 获取该目录下面的所有文件
    lists.sort(key=lambda fn: os.path.getatime(result_dir + "\\" + fn))
    # 找到最新生成的文件
    file_new = os.path.join(result_dir, lists[-1])
    # 调用发邮件模块
    send_mail(file_new)


def creatsuite():
    '''将用例添加到测试套件'''
    testunit = unittest.TestSuite()
    # 定义测试文件查找的目录
    test_dir = './test_case'
    # 定义discover方法的参数
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py', top_level_dir=None)
    # discover方法筛选出来的用例，循环添加到测试套件中

    return discover


if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    testreport = './report'
    filename = './report/ {0} result.html'.format(now)
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title="2017年7月18日ui自动化测试报告", description="运行环境 Windows7 Chrome浏览器")
    alltestnames = creatsuite()
    runner.run(alltestnames)
    fp.close()  # 关闭生成的报告
    send_report(testreport)  # 发送报告