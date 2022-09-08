# -*- coding: utf-8 -*-
"""
@File: test_Library.py
@Author: peterpang
@Time: 2021/11/23 15:16
"""
import pytest
from PageObject.LibraryPage.library_page import LibraryPage
from PageObject.MePage.wallet_page import Wallet
from PageObject.DiscoverPage.discover_page import DiscoverPage
from config.setting import log


@pytest.mark.usefixtures("is_logined")
class TestLibrary:

    # 进入任务中心
    def test_enter_task_center_in_library(self, is_logined):
        log.info("开始执行测试用例test_enter_task_center_in_library")
        # 进入书架
        LibraryPage(is_logined).click_library()
        # 点击任务中心
        LibraryPage(is_logined).click_task_center()
        # 断言,判断进入任务中心正确
        assert Wallet(is_logined).get_text_on_top() == "Earn Rewards"
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_task_center_in_library")

    # 进入延时解锁
    def test_enter_delay_unlock_in_library(self, is_logined):
        log.info("开始执行测试用例test_enter_delay_unlock_in_library")
        # 进入书架
        LibraryPage(is_logined).click_library()
        # 点击延时解锁
        LibraryPage(is_logined).click_delay()
        # 断言,判断进入延时解锁
        assert DiscoverPage(is_logined).is_delay_unlock_exist() == True
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_task_center_in_library")

    # 进入消息中心
    def test_enter_inbox_in_library(self, is_logined):
        log.info("开始执行测试用例test_enter_inbox_in_library")
        # 进入书架
        LibraryPage(is_logined).click_library()
        # 点击消息中心
        LibraryPage(is_logined).click_inbox_in_library()
        # 断言,判断已经进入任务中心
        assert Wallet(is_logined).get_text_on_top() == "Inbox"
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_inbox_in_library")

    # 进入下载中心
    def test_enter_download_in_library(self, is_logined):
        log.info("开始执行测试用例test_enter_download_in_library")
        # 进入书架
        LibraryPage(is_logined).click_library()
        # 点击下载中心
        LibraryPage(is_logined).click_download_in_library()
        # 断言,判断已经进入下载中心
        assert Wallet(is_logined).get_text_on_top() == "Downloads"
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_download_in_library")

    # 进入阅读记录
    def test_enter_viewed_in_library(self, is_logined):
        log.info("开始执行测试用例test_enter_viewed_in_library")
        # 进入书架
        LibraryPage(is_logined).click_library()
        # 点击下载中心
        LibraryPage(is_logined).click_viewed_in_library()
        # 断言,判断已经进入阅读记录
        assert Wallet(is_logined).get_text_on_top() == "Viewed"
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_viewed_in_library")

    # 编辑书架的书籍(待思考用例设计)
    # 进入书架中的书籍
    def test_enter_book_in_library(self, is_logined):
        log.info("开始执行测试用例test_enter_book_in_library")
        # 进入书架
        LibraryPage(is_logined).click_library()
        # 点击下载中心
        LibraryPage(is_logined).click_viewed_in_library()
        # 断言,判断已经进入阅读记录
        assert Wallet(is_logined).get_text_on_top() == "Viewed"
        # 返回上一层
        Wallet(is_logined).click_back()
        log.info("完成测试用例test_enter_book_in_library")


if __name__ == "__main__":
    pytest.main(["-s", f"{__file__}::TestLibrary"])
