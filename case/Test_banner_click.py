#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/23 23:39
# 点击首页商品分类

import unittest
from pages.tuozhen_HomePage import HomePage

class bannerCase(unittest.TestCase):

    def setUp(self):

        pass

    def test_click1(self):
        HomePage().advisory_click()



    def tearDown(self):

        pass