# -*- coding: utf-8 -*-
"""
@File: topup_page.py
@Author: peterpang
@Time: 2021/10/27 11:35
"""
from common.BaseDriver import BaseDriver
from PageLocators.Locators_Me import Me


class Topup(BaseDriver):

    # Me-Top Up
    def click_topup(self):
        name = "进入商店页面"
        self.wait_element_visible(Me.btn_top_up, doc=name)
        self.click_element(Me.btn_top_up, doc=name)

    # 判断商店页面是否存在
    def is_topup_page_exist(self):
        """
        :return: True or False
        """
        name = "判断商店页面是否存在"
        print(type(Me.btn_pay_method))
        print(Me.btn_pay_method)
        if self.wait_element_visible(Me.btn_pay_method, doc=name):
            return True
        else:
            return False

    # 点击返回按钮
    def click_back(self):
        name = "点击返回按钮"
        self.wait_element_visible(Me.btn_back, doc=name)
        self.click_element(Me.btn_back, doc=name)
