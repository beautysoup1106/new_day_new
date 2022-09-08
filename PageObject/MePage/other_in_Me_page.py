# -*- coding: utf-8 -*-
"""
@File: other_in_Me_page.py
@Author: peterpang
@Time: 2021/10/27 17:09
"""
from PageLocators.Locators_Me import Me
from common.BaseDriver import BaseDriver


class OtherInMe(BaseDriver):

    # 进入任务中心页面
    def click_earnRewards(self):
        name = "进入任务中心页面"
        self.wait_element_visible(Me.btn_task, doc=name)
        self.click_element(Me.btn_task, doc=name)

    # 任务中心的points record
    def is_earnRewards_page_exist(self):
        """
        :return: True or False
        """
        name = "判断points record按钮是否存在"
        if self.is_element_visible(Me.btn_points_record, doc=name):
            return True
        else:
            return False

    # 进入卡券中心页面
    def click_mycoupon(self):
        name = "进入卡券中心页面"
        self.wait_element_visible(Me.btn_coupon, doc=name)
        self.click_element(Me.btn_coupon, doc=name)

    # 进入兑换中心页面
    def click_redemCode(self):
        name = "进入兑换中心页面"
        self.wait_element_visible(Me.btn_redemption_code, doc=name)
        self.click_element(Me.btn_redemption_code, doc=name)

    # 进入消息中心页面
    def click_inbox(self):
        name = "进入消息中心页面"
        self.wait_element_visible(Me.btn_inbox, doc=name)
        self.click_element(Me.btn_inbox, doc=name)

    # 进入阅读记录页面
    def click_viewed(self):
        name = "进入阅读记录页面"
        self.wait_element_visible(Me.btn_viewed, doc=name)
        self.click_element(Me.btn_viewed, doc=name)

    # 进入关注页面
    def click_following(self):
        name = "进入关注页面"
        self.wait_element_visible(Me.btn_following, doc=name)
        self.click_element(Me.btn_following, doc=name)

    # 进入下载中心页面
    def click_downloads(self):
        name = "进入下载中心页面"
        self.wait_element_visible(Me.btn_downloads, doc=name)
        self.click_element(Me.btn_downloads, doc=name)

    # 进入成为作者页面
    def click_2bwriter(self):
        name = "进入成为作者页面"
        self.wait_element_visible(Me.btn_writer, doc=name)
        self.click_element(Me.btn_writer, doc=name)

    # 进入反馈中心页面
    def click_feedback(self):
        name = "进入反馈中心页面"
        self.wait_element_visible(Me.btn_feedback, doc=name)
        self.click_element(Me.btn_feedback, doc=name)

    # 进入设置页面
    def click_setting(self):
        name = "进入设置页面"
        self.wait_element_visible(Me.btn_setting, doc=name)
        self.click_element(Me.btn_setting, doc=name)
