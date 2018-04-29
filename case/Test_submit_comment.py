#!usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/29 09:33
# 提交资讯评论

import unittest
from base.appium_server import On_server
from pages.tuozhen_HomePage import HomePage
from pages.tuozhen_NewsdetailPage import NewsdetailPage
from pages.tuozhen_LoginPage import LoginPage
from pages.tuozhen_MyPage import MyPage

class commentCase(unittest.TestCase):

    def setUp(self):
        self.driver = On_server().get_driver()


    def test_submit(self):
        HP = HomePage(self.driver)
        HP.hot_news_click()
        NP = NewsdetailPage(self.driver)
        NP.comment_click()
        LP = LoginPage(self.driver)
        LP.login()
        NP.comment_submit_click()
        NP.back()
        HP.my_click()
        MP = MyPage(self.driver)
        MP.quit_click()

    def tearDown(self):
        self.driver.quit()