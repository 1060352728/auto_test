#!/usr/bin/env python
# -*- coding:utf-8 -*-
# author:likui

# 登录

from selenium import webdriver
import time


class Login_Case:

    def __init__(self, driver):
        self.driver = driver

    def login_curres(self, user, passwd):
        '''登录成功'''
        self.driver.switch_to_frame("x-URS-iframe")
        self.by_id("//input[@name='email']").clear()
        self.by_id("//input[@name='email']").send_keys(user)
        self.by_id("//input[@name='password']").clear()
        self.by_id("//input[@name='password']").send_keys(passwd)
        self.by_id(".//*[@id='dologin']").click()
        return self.driver

    def logout(self):
        '''退出登录'''
        self.by_id(".//*[@id='_mail_component_41_41']/a").click()

    def by_id(self, the_id):
        return self.driver.find_element_by_xpath(the_id)