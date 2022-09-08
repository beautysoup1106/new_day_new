# -*- coding: utf-8 -*-
"""
@File: wallet_page.py
@Author: peterpang
@Time: 2021/10/25 16:43
"""
from common.BaseDriver import BaseDriver
from PageLocators.Locators_Me import Me


class Wallet(BaseDriver):

    # Me-wallet
    def click_wallet(self):
        name = "进入钱包页面"
        self.wait_element_visible(Me.btn_wallet, doc=name)
        self.click_element(Me.btn_wallet, doc=name)

    # 判断钱包页面是否存在
    def is_wallet_page_exist(self):
        """
        :return: True or False
        """
        name = "判断钱包页面是否存在"
        if self.is_element_visible(Me.trans_his, doc=name):
            return True
        else:
            return False

    # Me-wallet-Transaction History
    def click_trans_his(self):
        name = "进入钱包的交易历史"
        self.wait_element_visible(Me.trans_his, doc=name)
        self.click_element(Me.trans_his, doc=name)

    # 获取顶部标题
    def get_text_on_top(self):
        """
        :return: text
        """
        name = "获取顶部标题"
        self.wait_element_visible(Me.title_text, doc=name)
        text = self.get_text(Me.title_text, doc=name)
        return text

    # 点击返回按钮
    def click_back(self):
        name = "点击返回按钮"
        self.wait_element_visible(Me.btn_back, doc=name)
        self.click_element(Me.btn_back, doc=name)

    # Me-wallet-Bonus Received
    def click_bonus_rec(self):
        name = "进入钱包的金券记录"
        self.wait_element_visible(Me.bonus_rec, doc=name)
        self.click_element(Me.bonus_rec, doc=name)

    # Me-wallet-Episodes Unlocked
    def click_episodes_unl(self):
        name = "进入钱包的解锁章节记录"
        self.wait_element_visible(Me.episodes_unl, doc=name)
        self.click_element(Me.episodes_unl, doc=name)

    # Me-wallet-Reward Record
    def click_reward_rec(self):
        name = "进入钱包的奖励记录"
        self.wait_element_visible(Me.reward_rec, doc=name)
        self.click_element(Me.reward_rec, doc=name)

    # 开关自动解锁按钮(待解决如何判断开关是开的还是关的)
    def turn_on_auto_unlock(self):
        name = "开关自动解锁按钮"
        self.wait_element_visible(Me.turn_on_auto_unl, doc=name)
        self.click_element(Me.turn_on_auto_unl, doc=name)
