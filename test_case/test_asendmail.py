#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:tian

import unittest
from selenium import webdriver
from time import sleep
from login import Login_Case


class Test_Send_Mail(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        base_url = "http://mail.126.com/"
        cls.driver.get(base_url)
        # cls.driver.implicitly_wait(10)
        sleep(10)

    def obj_metcho(self):
        obj = Login_Case(Test_Send_Mail.driver)
        return obj

    def test_alogin_surcee(self):
        '''登录进入123邮箱'''
        username = 'test_tx'
        password = "xxxxxxxx"
        login_obj = self.obj_metcho()

        title = self.driver.title
        print("登录前title:{0}".format(title))
        url = self.driver.current_url
        print("登录前url:{0}".format(url))

        driver = login_obj.login_curres(username, password)
        driver.switch_to_default_content()
        sleep(5)
        url = self.driver.current_url
        print("登录成功后url:{0}".format(url))
        print("登录成功后的title:{0}".format(self.driver.title))
        self.result = self.by_id("//span[@id='spnUid']").text
        self.assertTrue(username in self.result)

    def test_bwrite(self):
        '''写邮件输入收件人、主题、正文'''
        driver = self.driver
        # 点击左上角的写信按钮
        self.by_id("//*[@id='dvNavTop']/ul/li[2]/span[2]").click()
        sleep(5)

        # 输入收件人email地址
        self.by_id("//*[@role='combobox']").send_keys("352932341@qq.com")
        sleep(5)

        # 选中主题文本，输入主题内容；
        self.by_id("//input[@class='nui-ipt-input' and @type='text' and @maxlength='256']").click()
        self.by_id("//input[@class='nui-ipt-input' and @type='text' and @maxlength='256']").send_keys("我是自动化测试发邮件给你的啊")

        # 主题第二种定位方式
        # self.by_id(".//*[@class='bz0']/div[1]/input[@class='nui-ipt-input']").click()
        # self.by_id(".//*[@class='bz0']/div[1]/input[@class='nui-ipt-input']").send_keys("我是自动化发给你的邮件谢谢你光临")
        sleep(5)
        # 定位到正文iframe中
        class_name = self.by_id("//*[@class='APP-editor-iframe']")
        driver.switch_to_frame(class_name)
        driver.find_element_by_tag_name("body").send_keys("hi,all 各位小伙伴本次ui自动化测试通过了")
        # .//*[@class='jp0']/div[1]/span[2]
        driver.switch_to_default_content()
        self.by_id("//*[@class='jp0']/div[1]/span[2]").click()
        sleep(10)
        text = self.by_id("//*[@class='tK1' and @role='tooltip']").text
        self.assertIn(text, "发送成功可用手机接收回复免费短信通知")

    def test_csend_mail(self):
        '''只填写收件人发送邮件'''

        # 点击继续写信
        self.by_id("//*[@class='py1']/a[3]").click()
        # 输入收件人邮箱
        self.by_id("//*[@class='bz0']/div[2]/div[1]/input").send_keys("352932341@qq.com")
        sleep(5)
        # 点击发送按钮
        self.by_id("//*[@class='jp0']/div[1]/span[2]").click()
        sleep(5)
        # 确定不输入主题和正文的弹窗
        self.by_id("//*[@class='nui-msgbox-ft-btns']/div[1]/span").click()
        sleep(5)
        text = self.by_id("//*[@class='sQ1']/h1").text
        self.assertIn("发送成功", text)

    def test_dsend_mail(self):
        '''只填写收件人与主题发送'''
        self.by_id("//*[@class='py1']/a[3]").click()  # 点击继续写信
        # self.by_id("//*[@id='dvNavTop']/ul/li[2]/span[2]").click() #直接登录后，点击写信
        # 输入收件人邮箱
        self.by_id("//*[@class='bz0']/div[2]/div/input").send_keys("352932341@qq.com")
        sleep(5)
        # 输入主题
        self.by_id("//*[@class='nui-ipt-input' and @maxlength='256']").click()
        self.by_id("//*[@class='nui-ipt-input' and @maxlength='256']").send_keys("我只输入的主题没有输入正文")
        sleep(5)
        # 点击发送按钮
        self.by_id("//*[@class='jp0']/div[1]/span[2]").click()
        sleep(5)
        # 获取发送成功后的文本信息
        text = self.by_id("//*[@class='sQ1']/h1").text
        self.assertIn("发送成功", text)

    def test_esend_mail(self):
        '''输入收件人、主题、附件'''
        self.by_id("//*[@class='py1']/a[3]").click()  # 点击继续写信
        # 下面代码是，重新登录进入的
        # self.by_id("//*[@id='dvNavTop']/ul/li[2]/span[2]").click()
        # 输入收件人邮箱
        sleep(5)
        self.by_id("//*[@class='bz0']/div[2]/div/input").send_keys("352932341@qq.com")
        sleep(5)
        # 输入主题
        self.by_id("//*[@class='nui-ipt-input' and @maxlength='256']").click()
        self.by_id("//*[@class='nui-ipt-input' and @maxlength='256']").send_keys("我输入了主题且添加了附件")
        # 添加上传附件
        self.by_id("//*[@class='O0']").send_keys("E:\\test_email.txt")
        sleep(5)
        # 点击发送按钮
        self.by_id("//*[@class='jp0']/div[1]/span[2]").click()
        sleep(5)
        # 获取发送成功后的文本信息
        text = self.by_id("//*[@class='sQ1']/h1").text
        self.assertIn("发送成功", text)

    def test_clogin(self):
        '''退出登录'''
        logout_text = "您已成功退出网易邮箱。"
        self.obj_metcho().logout()
        sleep(10)
        self.result = self.by_id("html/body/section/h1").text
        self.assertEqual(logout_text, self.result)

    def by_id(self, the_id):
        return self.driver.find_element_by_xpath(the_id)

    def tearDownClass(cls):
        '''关闭浏览器'''
        cls.driver.quit()