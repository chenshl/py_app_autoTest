#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/22 23:32
# appium的webdriver参数设置

from appium import webdriver

class On_server(object):

    def __init__(self):
        desired_caps = {
                        'platformName': 'Android',
                        'deviceName': 'hol_t00',
                        'platformVersion': '4.2.2',
                        # 'appPackage': 'com.android.jinvovocni',
                        # 'appActivity': 'com.android.jinvovocni.ui.login.WelcomeActivity',
                        'appPackage': 'com.tuozhen.health',
                        'appActivity': 'com.tuozhen.health.activity.LaunchActivity',
                        'unicodeKeyboard': 'True',
                        'resetKeyboard': 'True'
                        }
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)

    def get_driver(self):
        return self.driver