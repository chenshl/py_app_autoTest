#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/25 21:46
# 登录页面

from appium import webdriver
from base.appium_server import On_server
from base.Element import Element

class LoginPage(Element):

    # 登录手机号码
    phoneNo_xpath = "//android.widget.EditText[contains(@text,'手机号码')]"
    # phoneNo_xpath = '手机号码'
    userName = "18716201367"
    # 登录密码
    password_xpath = "//android.widget.TextView[contains(@text, '忘记密码?')]/preceding-sibling::android.widget.EditText"
    password = "123456"
    # 登录按钮
    loginButton_class = "android.widget.Button"


    def login(self):

        self.get_xpath(self.phoneNo_xpath).send_keys(self.userName)
        self.get_xpath(self.password_xpath).send_keys(self.password)
        self.get_classes(self.loginButton_class)[0].click()

