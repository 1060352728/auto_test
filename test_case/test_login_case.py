from selenium import webdriver
from time import sleep
import unittest


class TestCase(unittest.TestCase):
    driver = webdriver.Chrome()

    @classmethod
    def setUpClass(cls):
        driver = cls.driver
        base_url = "https://mail.126.com/"
        driver.get(base_url)
        sleep(5)

    def test_eoagin_success(self):
        '''登录成功'''
        # Arrang  准备测试数据
        user_name = "lk1060352728"
        password = "lk123456789"
        loging_succeed_url = "wp-admin"
        sleep(5)
        # Action  执行测试步骤
        self.by_xpath("//input[@name='email']").clear()
        self.by_xpath("//input[@name='email']").send_keys(user_name)
        self.by_xpath("//input[@name='password']").clear()
        self.by_xpath("//input[@name='password']").send_keys(password)
        self.by_xpath("//input[@id='dologin']").click()
        sleep(5)
        # Assert  断言
        self.assertTrue(loging_succeed_url in self.driver.current_url)  # 登录成功后页面发生跳转后,断言url中是否wp-admin
        print("断言1 登录成功跳转url：{0}".format(self.driver.current_url))
        # Assert 断言2 登录成功后断言右上角是否存在admin
        greek_link = self.by_css("#wp-admin-bar-my-account >.ab-item").text
        print("断言2 greek_link:{0}".format(greek_link))
        self.assertTrue(user_name in greek_link)

    def test_ausername_passwor_all_null(self):
        '''用户名和密码为空'''
        # Action
        self.by_css("#user_login").send_keys()
        self.by_css("#user_pass").send_keys()
        self.by_css("#wp-submit").click()
        # Assert 断言
        self.assertTrue("wordpress/wp-login.php" in self.driver.current_url)

    def test_buser_password_null(self):
        '''输入正确用户名,密码为空'''
        # Arrang  准备测试数据
        username = "admin"
        login_error = "错误：密码一栏为空。"
        # Action 执行测试步骤
        self.by_css("#user_login").send_keys(username)
        self.by_css("#user_pass").send_keys()
        self.by_css("#wp-submit").click()

        # Assert 断言
        mesage_error = self.by_css("#login_error").text
        self.assertTrue(login_error in mesage_error)

    def test_cuser_password_error(self):
        '''正确的用户名，错误的密码'''
        # Arrang   准备测试数据
        sleep(3)
        username = "admin"
        password = "adafdanfn"
        login_error = "错误：admin 的密码不正确。"
        # Action 执行测试步骤
        self.by_css("#user_login").clear()
        self.by_css("#user_login").send_keys(username)
        self.by_css("#user_pass").send_keys(password)
        self.by_css("#wp-submit").click()
        # Assert 断言
        mesage_error = self.by_css("#login_error").text
        self.assertTrue(login_error in mesage_error)

    def test_duserpassword_error(self):
        '''用户名错误，密码错误'''
        # Arrang  准备测试数据
        sleep(3)
        username = "amdinjj"
        password = "112344"
        login_error = "错误：无效用户名。"
        # Action 执行测试步骤
        self.by_css("#user_login").clear()
        self.by_css("#user_login").send_keys(username)
        self.by_css("#user_pass").send_keys(password)
        self.by_css("#wp-submit").click()
        # Assert 断言
        message_error = self.by_css("#login_error").text
        self.assertTrue(login_error in message_error)

    def by_xpath(self, the_xpath):
        return self.driver.find_element_by_xpath(the_xpath)

    def by_css(self, the_css):
        return self.driver.find_element_by_css_selector(the_css)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()