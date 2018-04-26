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
    # phoneNo_xpath = "//android.widget.EditText[contains(@text,'手机号码')]"
    phoneNo_xpath = '手机号码'
    userName = "18716201367"
    # 登录密码
    password_xpath = "//android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout" \
                     "/android.widget.LinearLayout[4]/android.widget.EditText[@contains(@index,0)]"
    password = "123456"
    # 登录按钮
    loginButton_class = "android.widget.Button"


    def login(self):
        # Element.get_xpath(self.phoneNo_xpath).send_keys(self.userName)
        # Element.get_name(self.phoneNo_xpath).click()
        # Element.get_xpath(self.password_xpath).send_keys(self.password)
        # Element.get_classes(self.loginButton_class)[0].click()

        # self.driver.find_element_by_class_name(self.loginButton_class).click()
        self.get_classes(self.loginButton_class)[0].click()

