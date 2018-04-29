#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/28 22:05
# "我的"页面

from appium import webdriver
from base.Element import Element

class MyPage(Element):

    #退出登录按钮
    quit_button = "//android.widget.Button[contains(@text, '退出登录')]"

    #点击退出登录
    def quit_click(self):
        self.swipe_to_up()  #上滑
        self.wait_for_xpath(self.quit_button)  #等待退出按钮
        self.get_xpath(self.quit_button).click()