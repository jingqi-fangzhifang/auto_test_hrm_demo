#!/usr/bin/env python
#-- coding: utf-8 --
"""
测试selenium demo

"""

from selenium import webdriver
import unittest
import time


current_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
pic_path = 'D:\\workplace\\imgs\\' + current_time  + '.png'

class TestSelenium(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.base_url = "https://aijuhr.com/login/"

        self.verificationErrors = []
        self.accept_next_alert = True

    def test_login(self):
        driver = self.driver

        driver.get(self.base_url)
        driver.find_element_by_css_selector('#login_wrap > div > div.passwordLogin > div.login_user > input[type="text"]').send_keys('18368180275')
        driver.find_element_by_css_selector('#login_wrap > div > div.passwordLogin > div.login_pass > input[type="password"]').send_keys('jingqi123')
        driver.find_element_by_css_selector('#login_wrap > div > div.passwordLogin > div.login_submit > button').click()

        #driver.save_screenshot(pic_path)

    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()