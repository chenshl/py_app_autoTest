#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/24 23:42
# 拓诊用户APP首页

from appium import webdriver
from base.Element import Element

class HomePage(Element):

    #我的咨询class
    advisory_class = 'android.widget.RelativeLayout'
    button_my = "//android.widget.Button[contains(@text, '我的')]"


    #点击我的咨询
    def advisory_click(self):
        self.wait_for_xpath(self.button_my)  #等待页面精确元素
        self.get_classes(self.advisory_class)[4].click()

    #点击我的
    def my_click(self):
        self.get_xpath(self.button_my).click()
