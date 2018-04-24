#!/usr/bin/python
# coding:utf-8
# @author : csl
# @date   : 2018/04/23 20:40
# 基础操作

from appium import webdriver
from base.appium_server import On_server
from appium.webdriver.mobilecommand import MobileCommand
import time

class Element(object):
    #获取driver
    def __init__(self):
        self.driver = On_server().get_driver()

    #ID定位
    def get_id(self, id):
        element = self.driver.find_element_by_id(id)
        return element

    #name定位
    def get_name(self, name):
        element = self.driver.find_element_by_name(name)
        return element

    #退出
    def over(self):
        element = self.driver.quit()
        return element

    #截图
    # def get_screen(self, path):
        # self.driver.get_screenshot_as_file(path)
    def get_screen(self, name):
        day = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        fp = "..\\Result\\" + day
        tm = time.strftime('%Y-%m-%d-%H_%M_%S', time.localtime(time.time()))
        type = '.png'

        filename = ''
        if os.path.exists(fp):
            filename = fp + "\\" + tm + '_' + name + type
        else:
            os.makedirs(fp)
            filename = fp + "\\" + tm + '_' + name + type
        self.driver.save_screenshot(filename)


    #获取屏幕的宽和高
    def get_size(self):
        size = self.driver.get_window_size()
        return size

    #上滑，从坐标1滑动到坐标2，t毫秒时间内完成
    def swipe_to_up(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

    #下滑
    def swipe_to_down(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

    #左滑
    def swipe_to_left(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

    #右滑
    def swipe_to_right(self):
        window_size = self.get_size()
        width = window_size.get("width")
        height = window_size.get("height")
        self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

    #手机返回键
    def back(self):
        self.driver.keyevent(4)

    #class定位
    def get_classes(self, classesname):
        elements = self.driver.find_elements_by_class_name(classesname)
        return elements

    #定位ID队列（返回一个list）
    def get_ids(self, ids):
        elements = self.driver.find_elements_by_id(ids)
        return elements

    #切换到H5的webdriver
    def switch_h5(self):
        # self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "WEBVIEW_com.weizq"})
        self.driver.switch_to.context(WEBVIEW)

    #切换到APP的webdriver
    def switch_app(self):
        self.driver.execute(MobileCommand.SWITCH_TO_CONTEXT, {"name": "NATIVE_APP"})

    #定位H5页面xpath返回列表
    def get_xpath(self, xpath):
        elements = self.driver.find_elements_by_xpath(xpath)
        return elements


