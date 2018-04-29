#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/29 09:04
# 新闻详情页面

from appium import webdriver
from base.Element import Element

class NewsdetailPage(Element):

    #评论框
    comment = "//android.widget.EditText[contains(@text, '说两句')]"
    comment_comment = "很好的移动医疗平台"
    submit_comment = "//android.widget.Button[contains(@text, '提交评论')]"

    #提交评论
    def comment_click(self):
        self.get_xpath(self.comment).send_keys(self.comment_comment)
        self.wait_for_xpath(self.submit_comment)
        self.get_xpath(self.submit_comment).click()

    #登录后返回直接提交
    def comment_submit_click(self):
        self.wait_for_xpath(self.submit_comment)
        self.get_xpath(self.submit_comment).click()