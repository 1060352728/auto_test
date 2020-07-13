#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:tian

import unittest
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
from login import Login_Case


class DeletEmail(unittest.TestCase):
    ''' 删除邮件'''
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        driver = cls.driver
        driver.maximize_window()
        base_url = "http://mail.126.com/"
        driver.get(base_url)
        sleep(10)

    def obj_methond(self):
        obj = Login_Case(DeletEmail.driver)
        return obj

    # 登录126邮箱
    def test_alogin(self):
        username = "test_tx"
        password = "123456tian"
        obj_driver = self.obj_methond()
        driver = obj_driver.login_curres(username, password)
        driver.switch_to_default_content()
        sleep(10)
        self.result = self.by_id("//*[@id='spnUid']").text
        self.assertTrue(username in self.result)

    @StopIteration
    def test_bdelete_email(self):
        '''删除邮件'''
        sleep(5)
        self.driver.find_element_by_class_name("nui-tree-item-text").click()
        sleep(3)
        self.driver.find_elements_by_xpath("//span[@class='nui-chk-symbol']/b").pop(1).click()
        sleep(5)
        try:
            spans = self.driver.find_elements_by_tag_name('span')
            for i in spans:
                if i.text == "删 除":
                    i.click()

        except Exception as e:
            print("找不到删除按钮")
        sleep(3)
        # 断言是否已删除
        text = self.driver.find_element_by_css_selector("span.nui-tips-text>a").text
        self.assertEqual(text, '已删除')

    def test_logout(self):
        '''退出登录'''
        logout_text = "您已成功退出网易邮箱。"
        self.obj_methond().logout()
        sleep(10)
        self.result = self.by_id("html/body/section/h1").text
        self.assertEqual(logout_text, self.result)

    def by_id(self, the_id):
        return self.driver.find_element_by_xpath(the_id)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()