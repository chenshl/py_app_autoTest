#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/23 23:39
# 点击首页商品分类

import unittest
from base.appium_server import On_server
from pages.tuozhen_HomePage import HomePage
from pages.tuozhen_LoginPage import LoginPage
from pages.tuozhen_MyPage import MyPage
import time

class bannerCase(unittest.TestCase):

    def setUp(self):
        #获取当前driver
        self.driver = On_server().get_driver()


    def test_click1(self):
        HP = HomePage(self.driver)
        HP.advisory_click()
        LP = LoginPage(self.driver)
        LP.login()
        time.sleep(2)  #等待2秒加载数据
        LP.back()
        HP.my_click()
        MP = MyPage(self.driver)
        MP.quit_click()


    def tearDown(self):
        self.driver.quit()