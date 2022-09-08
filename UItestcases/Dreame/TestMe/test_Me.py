# -*- coding: utf-8 -*-
"""
@File: test_Me.py
@Author: peterpang
@Time: 2021/10/27 17:24
"""
import time

import pytest
from PageObject.MePage.other_in_Me_page import OtherInMe
from PageObject.MePage.Login_page import Login
from PageObject.MePage.wallet_page import Wallet
from config.setting import log


@pytest.mark.usefixtures("is_logined")
class TestMe:

    # Me-Earn Rewards
    def test_enter_earnRewards(self, is_logined):
        log.info("开始执行测试用例test_enter_earnRewards")
        # 点击me页面
        Login(is_logined).click_Me()
        # 点击Earn Rewards
        OtherInMe(is_logined).click_earnRewards()
        # 断言,判断已经进入任务中心
        assert OtherInMe(is_logined).is_earnRewards_page_exist() == True
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_earnRewards")

    # Me-My Coupons
    def test_enter_myCoupons(self, is_logined):
        log.info("开始执行测试用例test_enter_myCoupons")
        # 点击me页面
        Login(is_logined).click_Me()
        # 点击My Coupons
        OtherInMe(is_logined).click_mycoupon()
        # 断言,判断已经进入任务中心
        assert Wallet(is_logined).get_text_on_top() == "My Coupons"
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_myCoupons")

    # Me-Redemption Code
    def test_enter_redemCode(self, is_logined):
        log.info("开始执行测试用例test_enter_redemCode")
        # 点击me页面
        Login(is_logined).click_Me()
        # 点击Redemption Code
        OtherInMe(is_logined).click_redemCode()
        # 断言,判断已经进入任务中心
        assert Wallet(is_logined).get_text_on_top() == "Redemption Code"
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_redemCode")

    # Me-Inbox
    def test_enter_inbox(self, is_logined):
        log.info("开始执行测试用例test_enter_inbox")
        # 点击me页面
        Login(is_logined).click_Me()
        # 点击Inbox
        OtherInMe(is_logined).click_inbox()
        # 断言,判断已经进入任务中心
        assert Wallet(is_logined).get_text_on_top() == "Inbox"
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_inbox")

    # Me-viewed
    def test_enter_viewed(self, is_logined):
        log.info("开始执行测试用例test_enter_viewed")
        # 点击me页面
        Login(is_logined).click_Me()
        # 点击viewed
        OtherInMe(is_logined).click_viewed()
        # 断言,判断已经进入阅读记录
        assert Wallet(is_logined).get_text_on_top() == "Viewed"
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_viewed")

    # Me-Following
    def test_enter_following(self, is_logined):
        log.info("开始执行测试用例test_enter_following")
        # 点击me页面
        Login(is_logined).click_Me()
        # 点击Following
        OtherInMe(is_logined).click_following()
        # 断言,判断已经进入任务中心
        assert Wallet(is_logined).get_text_on_top() == "Following"
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_following")

    # Me-Downloads
    def test_enter_downloads(self, is_logined):
        log.info("开始执行测试用例test_enter_downloads")
        # 点击me页面
        Login(is_logined).click_Me()
        # 点击downloads
        OtherInMe(is_logined).click_downloads()
        # 断言,判断已经进入任务中心
        assert Wallet(is_logined).get_text_on_top() == "Downloads"
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_downloads")

    # Me-To be a Dreame Writer!
    def test_enter_toBeWriter(self, is_logined):
        log.info("开始执行测试用例test_enter_toBeWriter")
        # 点击me页面
        Login(is_logined).click_Me()
        # 点击To be Dreame Writer!
        OtherInMe(is_logined).click_2bwriter()
        # 断言,判断已经进入任务中心
        assert Wallet(is_logined).get_text_on_top() == "To be a Dreame Writer!"
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_toBeWriter")

    # Me-Feedback
    def test_enter_feedback(self, is_logined):
        log.info("开始执行测试用例test_enter_feedback")
        # 点击me页面
        Login(is_logined).click_Me()
        # 点击Feedback
        OtherInMe(is_logined).click_feedback()
        # 断言,判断已经进入任务中心
        assert Wallet(is_logined).get_text_on_top() == "Feedback"
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_feedback")

    # Me-Setting(检查是否需要增加往上滑动的操作)
    def test_enter_setting(self, is_logined):
        log.info("开始执行测试用例test_enter_setting")
        # 点击me页面
        Login(is_logined).click_Me()
        # 点击Earn Rewards
        OtherInMe(is_logined).click_setting()
        # 断言,判断已经进入任务中心
        assert Wallet(is_logined).get_text_on_top() == "Setting"
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_setting")


if __name__ == '__main__':
    pytest.main(["-s", f"{__file__}::TestMe"])
