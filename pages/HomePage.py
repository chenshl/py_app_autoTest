#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/23 22:39
# 长青APP首页

from base.Element import Element
from appium import webdriver

class HomePage(object):

    #定位元素H5
    #分类列表
    classification = '//div[@class="home_slidenav"]'

    #定位元素APP
    more_class = "android.widget.LinearLayout"

    # #点击banner
    # def banner_click(self):
    #     wb = Element()
    #     wb.switch_h5()
    #     wb.get_xpath(classification).click()

    def more_class_click(self):
        wb = Element()
        # wb.get_classes(self.more_class)[1].click()
        # Element.switch_h5()
        # wb1 = wb.get_classes(self.classification)
        wb.switch_h5()
        wb1 = wb.get_xpath(self.classification)
        wb1[0].click()








