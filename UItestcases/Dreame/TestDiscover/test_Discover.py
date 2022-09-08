# -*- coding: utf-8 -*-
"""
@File: test_Discover.py
@Author: peterpang
@Time: 2021/10/29 14:53
"""
import pytest
from PageObject.DiscoverPage.discover_page import DiscoverPage
from PageObject.MePage.topup_page import Topup
from PageObject.MePage.wallet_page import Wallet
from config.setting import log
# noinspection PyBroadException


@pytest.mark.usefixtures("is_logined")
class TestDiscover:

    # 进入搜索页
    def test_enter_search_in_discover(self, is_logined):
        log.info("开始执行测试用例test_enter_search_in_discover")
        # 点击进入Discover模块
        DiscoverPage(is_logined).click_discover()
        # 点击搜索框
        DiscoverPage(is_logined).click_search()
        # 断言,判断已进入搜索框
        assert DiscoverPage(is_logined).is_search_exist() == True
        # 点击取消按钮
        DiscoverPage(is_logined).click_cancel_in_search()
        log.info("完成测试用例test_enter_search_in_discover")

    # 进入延时解锁页
    def test_enter_delay_unlock_page(self, is_logined):
        log.info("开始执行测试用例test_enter_delay_unlock_page")
        # 点击进入Discover模块
        DiscoverPage(is_logined).click_discover()
        # 点击搜索框
        DiscoverPage(is_logined).click_delay_unlock()
        # 断言,判断已进入延时解锁页面
        assert DiscoverPage(is_logined).is_delay_unlock_exist() == True
        # 返回上一层
        DiscoverPage(is_logined).click_back()
        log.info("完成测试用例test_enter_delay_unlock_page")

    # 进入消息通知页
    def test_enter_inbox_page(self, is_logined):
        log.info("开始执行测试用例test_enter_inbox_page")
        # 点击进入Discover模块
        DiscoverPage(is_logined).click_discover()
        # 点击搜索框
        DiscoverPage(is_logined).click_inbox_in_discover()
        # 断言,判断已进入消息通知页面
        assert Wallet(is_logined).get_text_on_top() == "Inbox"
        # 返回上一层
        Topup(is_logined).click_back()
        log.info("完成测试用例test_enter_inbox_page")

    # 进入view all页
    def test_enter_view_all_page(self, is_logined):
        log.info("开始执行测试用例test_enter_view_all_page")
        # 点击进入Discover模块
        DiscoverPage(is_logined).click_discover()
        # 点击搜索框
        DiscoverPage(is_logined).click_view_all()
        # 断言,判断已进入搜索框
        assert DiscoverPage(is_logined).is_view_all_exist() == True
        # 返回上一层
        Topup(is_logined).click_back()
        log.info("完成测试用例test_enter_view_all_page")


if __name__ == '__main__':
    pytest.main(["-s", f"{__file__}::TestDiscover"])
