#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/24 23:42
# 拓诊用户APP首页

from appium import webdriver
from base.Element import Element
import time

class HomePage(Element):

    #我的咨询class
    advisory_class = 'android.widget.RelativeLayout'
    #“我的”按钮
    button_my = "//android.widget.Button[contains(@text, '我的')]"
    #热门资讯
    hot_news = "//android.widget.TextView[contains(@text, '热门资讯')]"
    #第一条新闻
    first_news = "//android.widget.TextView[contains(@text, '热门资讯')]/../following-sibling::android.widget.ListView/android.widget.LinearLayout[1]"


    #点击我的咨询
    def advisory_click(self):
        self.wait_for_xpath(self.button_my)  #等待页面精确元素
        self.get_classes(self.advisory_class)[4].click()

    #点击我的
    def my_click(self):
        self.wait_for_xpath(self.button_my)  # 等待页面精确元素
        self.get_xpath(self.button_my).click()

    #点击热门资讯
    def hot_news_click(self):
        self.wait_for_xpath(self.button_my)  # 等待页面精确元素
        time.sleep(2)  #页面元素后加载强制等待2秒
        for i in  range(1):
            self.swipe_to_up()
        self.wait_for_xpath(self.hot_news)
        self.get_xpath(self.first_news).click()



