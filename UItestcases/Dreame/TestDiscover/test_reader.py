# -*- coding: utf-8 -*-
"""
@File: test_reader.py
@Author: peterpang
@Time: 2021/11/5 9:45
"""
import time

import pytest
from config.setting import *
from PageObject.DiscoverPage.discover_page import DiscoverPage
from PageObject.DiscoverPage.reader_page import ReaderPage
from PageObject.MePage.topup_page import Topup
from PageObject.MePage.wallet_page import Wallet
# noinspection PyBroadException


@pytest.mark.usefixtures("is_logined")
class TestReader:

    # 进入书籍详情页
    def test_enter_book_detail_page(self, is_logined):
        log.info("开始执行测试用例test_enter_book_detail_page")
        # 点击进入Discover模块
        DiscoverPage(is_logined).click_discover()
        # 点击Discover频道
        DiscoverPage(is_logined).click_channel("Discover")
        # 点击一本书
        DiscoverPage(is_logined).click_book()
        # 断言,判断是否已进入书籍详情页
        assert ReaderPage(is_logined).is_book_detail_page_exist() == True
        # 返回上一页
        Topup(is_logined).click_back()
        log.info("结束测试用例test_enter_book_detail_page")

    # 进入书籍详情页的下载页面
    def test_enter_download_in_book_detail_page(self, is_logined):
        log.info("开始执行测试用例test_enter_download_in_book_detail_page")
        # 点击进入Discover模块
        DiscoverPage(is_logined).click_discover()
        # 点击Discover频道
        DiscoverPage(is_logined).click_channel("Discover")
        # 点击一本书
        DiscoverPage(is_logined).click_book()
        # 点击下载中心
        ReaderPage(is_logined).click_download_in_book_detail_page()
        # 断言,判断是否进入了下载中心
        assert ReaderPage(is_logined).is_download_page_exist() == True
        # 关闭下载中心
        ReaderPage(is_logined).click_close_in_download_page()
        # 返回上一页
        Topup(is_logined).click_back()
        log.info("结束测试用例test_enter_download_in_book_detail_page")

    # 进入书籍详情页的Report页面
    def test_enter_report_in_book_detail_page(self, is_logined):
        log.info("开始执行测试用例test_enter_report_in_book_detail_page")
        # 点击进入Discover模块
        DiscoverPage(is_logined).click_discover()
        # 点击Discover频道
        DiscoverPage(is_logined).click_channel("Discover")
        # 点击一本书
        DiscoverPage(is_logined).click_book()
        # 点击report
        ReaderPage(is_logined).click_report_in_book_detail_page()
        # 断言,判断是否进入了report页面
        assert Wallet(is_logined).get_text_on_top() == "Report this story"
        # 返回上一页
        Topup(is_logined).click_back()
        Topup(is_logined).click_back()
        log.info("结束测试用例test_enter_report_in_book_detail_page")

    # 进入书籍详情页的Share页面
    def test_enter_share_in_book_detail_page(self, is_logined):
        log.info("开始执行测试用例test_enter_share_in_book_detail_page")
        # 点击进入Discover模块
        DiscoverPage(is_logined).click_discover()
        # 点击Discover频道
        DiscoverPage(is_logined).click_channel("Discover")
        # 点击一本书
        DiscoverPage(is_logined).click_book()
        # 点击report
        ReaderPage(is_logined).click_share_in_book_detail_page()
        # 断言,判断是否进入了share页面
        assert ReaderPage(is_logined).is_share_page_exist()
        # 返回上一页
        Topup(is_logined).click_back()
        Topup(is_logined).click_back()
        log.info("结束测试用例test_enter_share_in_book_detail_page")

    # 进入阅读器
    def test_enter_reader(self, is_logined):
        log.info("开始执行测试用例test_enter_reader")
        # 点击进入Discover模块
        DiscoverPage(is_logined).click_discover()
        # 点击Discover频道
        DiscoverPage(is_logined).click_channel("Discover")
        # 点击一本书
        DiscoverPage(is_logined).click_book()
        # 点击start reading
        ReaderPage(is_logined).click_start_read()
        # 断言,判断是否进入阅读器
        assert ReaderPage(is_logined).is_reader_page_exist() == True
        # 按压屏幕
        ReaderPage(is_logined).press_reader()
        # 返回上一层
        Topup(is_logined).click_back()
        Topup(is_logined).click_back()
        log.info("结束测试用例test_enter_reader")

    # 在阅读器点击下载中心
    def test_enter_download_in_reader(self, is_logined):
        log.info("开始执行测试用例test_enter_download_in_reader")
        # 点击进入Discover模块
        DiscoverPage(is_logined).click_discover()
        # 点击Discover频道
        DiscoverPage(is_logined).click_channel("Discover")
        # 点击一本书
        DiscoverPage(is_logined).click_book()
        # 点击start reading
        ReaderPage(is_logined).click_start_read()
        # 按压屏幕
        ReaderPage(is_logined).press_reader()
        # 点击下载中心
        ReaderPage(is_logined).click_download_in_book_detail_page()
        # 断言,判断是否进入了下载中心
        assert ReaderPage(is_logined).is_download_page_exist() == True
        # 关闭下载中心
        ReaderPage(is_logined).click_close_in_download_page()
        # 按压屏幕
        ReaderPage(is_logined).press_reader()
        # 返回上一层
        Topup(is_logined).click_back()
        Topup(is_logined).click_back()
        log.info("结束测试用例test_enter_download_in_book_detail_page")

    # 在阅读器解锁章节
    def test_unlock_episodes(self, is_logined):
        log.info("开始执行测试用例test_unlock_episodes")
        # 点击进入Discover模块
        DiscoverPage(is_logined).click_discover()
        # 点击Discover频道
        DiscoverPage(is_logined).click_channel("Discover")
        # 点击一本书
        DiscoverPage(is_logined).click_book()
        # 循环判断本书是否为付费书籍(有可能出现当前书籍被删除的场景)
        i = 1
        while i < 10:
            if ReaderPage(is_logined).get_tag_from_download_in_download_page() == 'FREE':
                # 翻到下一本书
                i += 1
            else:
                break
        # 点击start reading
        ReaderPage(is_logined).click_start_read()
        # 按压屏幕
        ReaderPage(is_logined).press_reader()
        # 点击章节展示
        ReaderPage(is_logined).click_menu_in_reader()
        # 获取付费章节数(需要补充当前页面没有解锁按钮的场景)***************
        nums = ReaderPage(is_logined).get_nums_of_pay_episodes()
        # 循环进入章节判断是否需要付费,需要的话则解锁,不需要则切换到下一章while
        i = 1
        while i < nums:
            # 点击付费章节
            ReaderPage(is_logined).click_pay_episodes(i)
            # 进入付费章节后判断是否存在解锁按钮
            if ReaderPage(is_logined).is_pay_btn_exist():
                # 如果存在则点击解锁
                time.sleep(2)
                ReaderPage(is_logined).click_pay_btn()
                time.sleep(3)
                # 断言判断解锁成功
                assert ReaderPage(is_logined).is_pay_btn_exist() == False
                break
            else:
                # 按压屏幕
                ReaderPage(is_logined).press_reader()
                # 点击章节展示
                ReaderPage(is_logined).click_menu_in_reader()
                i = i + 1
        # 按压屏幕
        ReaderPage(is_logined).press_reader()
        # 返回上一层
        Topup(is_logined).click_back()
        Topup(is_logined).click_back()
        log.info("结束测试用例test_unlock_episodes")

    # 评论章节
    def test_comment(self, is_logined):
        log.info("开始执行测试用例test_comment")
        # 点击进入Discover模块
        DiscoverPage(is_logined).click_discover()
        # 点击Discover频道
        DiscoverPage(is_logined).click_channel("Discover")
        # 点击一本书
        DiscoverPage(is_logined).click_book()
        # 点击start reading
        ReaderPage(is_logined).click_start_read()
        # 按压屏幕
        ReaderPage(is_logined).press_reader()
        # 点击评论
        ReaderPage(is_logined).click_comment()
        # 在评论输入框输入评论并发表
        ReaderPage(is_logined).input_content("nice story")
        # 获取评论第一条断言
        assert ReaderPage(is_logined).get_content() == "nice story"
        # 返回上一层
        Topup(is_logined).click_back()
        Topup(is_logined).click_back()
        Topup(is_logined).click_back()
        log.info("结束测试用例test_comment")


if __name__ == "__main__":
    pytest.main(["-s", f"{__file__}::TestReader"])
