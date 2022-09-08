# -*- coding: utf-8 -*-
"""
@File: test_enterWallet.py
@Author: peterpang
@Time: 2021/10/25 16:47
"""
import pytest
from PageObject.MePage.wallet_page import Wallet
from PageObject.MePage.Login_page import Login
from config.setting import log


@pytest.mark.usefixtures("is_logined")
class TestWallet:

    # 进入钱包页面
    def test_enter_wallet(self, is_logined):
        log.info("开始执行测试用例test_enter_wallet")
        # 点击me页面
        Login(is_logined).click_Me()
        # 进入wallet页面
        Wallet(is_logined).click_wallet()
        # 断言,判断已进入钱包页面
        assert Wallet(is_logined).is_wallet_page_exist() == True
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_wallet")

    # 进入钱包的交易记录页面
    def test_enter_trans_his(self, is_logined):
        log.info("开始执行测试用例test_enter_trans_his")
        # 点击me页面
        Login(is_logined).click_Me()
        # 进入wallet页面
        Wallet(is_logined).click_wallet()
        # 进入Transaction History页面
        Wallet(is_logined).click_trans_his()
        # 断言,判断已进入Transaction History页面
        assert Wallet(is_logined).get_text_on_top() == "Transaction History"
        # 返回上一层
        Wallet(is_logined).click_back()
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_trans_his")

    # 进入钱包的金券记录页面
    def test_enter_bonus_rec(self, is_logined):
        log.info("开始执行测试用例test_enter_bonus_rec")
        # 点击me页面
        Login(is_logined).click_Me()
        # 进入wallet页面
        Wallet(is_logined).click_wallet()
        # 进入Bonus Received页面
        Wallet(is_logined).click_bonus_rec()
        # 断言,判断已进入Bonus Received页面
        assert Wallet(is_logined).get_text_on_top() == "Bonus Received"
        # 返回上一层
        Wallet(is_logined).click_back()
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_bonus_rec")

    # 进入钱包的解锁章节记录页面
    def test_enter_episodes_unl(self, is_logined):
        log.info("开始执行测试用例test_enter_episodes_unl")
        # 点击me页面
        Login(is_logined).click_Me()
        # 进入wallet页面
        Wallet(is_logined).click_wallet()
        # 进入Episodes Unlocked页面
        Wallet(is_logined).click_episodes_unl()
        # 断言,判断已进入Episodes Unlocked页面
        assert Wallet(is_logined).get_text_on_top() == "Episodes Unlocked"
        # 返回上一层
        Wallet(is_logined).click_back()
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_episodes_unl")

    # 进入钱包的解锁章节记录页面
    def test_enter_reward_rec(self, is_logined):
        log.info("开始执行测试用例test_enter_reward_rec")
        # 点击me页面
        Login(is_logined).click_Me()
        # 进入wallet页面
        Wallet(is_logined).click_wallet()
        # 进入Reward Record页面
        Wallet(is_logined).click_reward_rec()
        # 断言,判断已进入Reward Record页面
        assert Wallet(is_logined).get_text_on_top() == "Reward record"
        # 返回上一层
        Wallet(is_logined).click_back()
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_reward_rec")


if __name__ == '__main__':
    pytest.main(["-s", f"{__file__}::TestWallet"])
