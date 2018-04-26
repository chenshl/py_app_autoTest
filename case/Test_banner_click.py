#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/23 23:39
# 点击首页商品分类

import unittest
from base.appium_server import On_server
from pages.tuozhen_HomePage import HomePage
from pages.tuozhen_LoginPage import LoginPage

class bannerCase(unittest.TestCase):

    def setUp(self):
        #获取当前driver
        self.driver = On_server().get_driver()


    def test_click1(self):
        HP = HomePage(self.driver)
        HP.advisory_click()
        LP = LoginPage(self.driver)
        LP.login()



    def tearDown(self):
        self.driver.quit()