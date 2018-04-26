#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/24 23:42
# 拓诊用户APP首页

from appium import webdriver
from base.appium_server import On_server
from base.Element import Element

class HomePage(Element):

    #我的咨询class
    advisory_class = 'android.widget.RelativeLayout'
    

    #点击我的咨询
    def advisory_click(self):
        self.get_classes(self.advisory_class)[4].click()
