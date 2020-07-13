# !/usr/bin/env python
# -*- coding:utf-8 -*-
# author:tian
import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from login import Login_Case


class Serach_email(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        cls.driver.maximize_window()
        base_url = "http://mail.126.com/"
        cls.driver.get(base_url)
        sleep(10)

    def obj_metcho(self):
        '''实例化Login_Case类'''
        obj = Login_Case(Serach_email.driver)
        return obj

    # 登录126.com邮箱
    def test_alogin_succer(self):
        user_name = "test_tx"
        password = "123456tian"
        login_obj = self.obj_metcho()
        driver = login_obj.login_curres(user_name, password)
        driver.switch_to_default_content()
        sleep(10)
        self.result = self.by_id("//*[@id='spnUid']").text
        self.assertTrue(user_name in self.result)

    def test_bserach_content(self):
        '''输入关键值点击搜索'''
        sleep(5)
        self.by_id("//*[@class='nui-ipt-input' and @type='text']").clear()
        self.by_id("//*[@class='nui-ipt-input' and @type='text']").send_keys("重置成功")
        self.by_id("//*[@class='nui-ipt-input' and @type='text']").send_keys(Keys.ENTER)
        sleep(10)
        self.result = self.by_id("//*[@class='tb0']/div/span").text
        print("self_result是多少啊", self.result)
        self.assertIn("重置成功", self.result)

    def test_cnot_serach(self):
        '''输入关键字不存在'''
        sleep(5)
        self.by_id("//*[@class='nui-ipt-input' and @type='text']").clear()
        self.by_id("//*[@class='nui-ipt-input' and @type='text']").send_keys("在哪了啊")
        self.by_id("//*[@class='nui-ipt-input' and @type='text']").send_keys(Keys.ENTER)
        sleep(10)
        self.result = self.by_id("//*[@class='rm1']").text
        self.assertIn("抱歉，没有搜索到", self.result)

    def test_dlogout(self):
        '''退出登录'''
        logout_text = "您已成功退出网易邮箱。"
        self.obj_metcho().logout()
        sleep(10)
        self.result = self.by_id("html/body/section/h1").text
        self.assertEqual(logout_text, self.result)

    def by_id(self, the_id):
        return self.driver.find_element_by_xpath(the_id)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()