# -*- coding: utf-8 -*-
"""
@File: discover_page.py
@Author: peterpang
@Time: 2021/10/29 9:25
"""
from common.BaseDriver import BaseDriver
from PageLocators.Locators_Discover import Discover
from config.setting import *


class DiscoverPage(BaseDriver):
    """书城页面相关操作"""

    # 点击Discover模块
    def click_discover(self):
        name = "点击Discover模块"
        self.wait_element_visible(Discover.btn_discover, doc=name)
        self.click_element(Discover.btn_discover, doc=name)

    # 选择频道
    def click_channel(self, channel=None):
        """
        根据频道名称选择一个频道,channel=None时选择第一个频道(即不选择频道)
        :param channel: 频道名称,默认为第一个频道
        :return:
        """
        name = "在书城选择一个频道"
        if channel is not None:
            self.wait_element_visible(Discover.choose_channel(channel), doc=name)
            self.click_element(Discover.choose_channel(channel), doc=name)

    # 在书城点击书籍
    def click_book(self, book_name=None):
        """
        先选择一个频道,再根据书籍名称点击一本书
        :param
        :param book_name: 书籍名称,默认为空,当输入书籍名称时则点击书籍名称
        :return:
        """
        name = "在书城点击书籍进入书籍详情页"
        # 如果传入了书籍名称,则点击对应的书籍名称,否则默认点击第一本书
        if book_name is not None:
            if self.is_element_visible(Discover.choose_book_by_name(book_name)):
                self.wait_element_visible(Discover.choose_book_by_name(book_name), doc=name)
                self.click_element(Discover.choose_book_by_name(book_name), doc=name)
            else:
                self.wait_element_visible(Discover.book_img, doc=name)
                self.click_element(Discover.book_img, doc=name)
        else:
            self.wait_element_visible(Discover.book_img, doc=name)
            self.click_element(Discover.book_img, doc=name)

    # 点击栏目的view all
    def click_view_all(self, column_name=None):
        """
        如果传了栏目,则选择对应栏目的view all,如果栏目不存在或者没有传,则选择第一个
        :param column_name: 栏目名称
        :return:
        """
        name = "在书城页点击view all"
        if column_name is not None:
            if self.is_element_visible(Discover.btn_view_all_by_column_name(column_name)):
                self.wait_element_visible(Discover.btn_view_all_by_column_name(column_name), doc=name)
                self.click_element(Discover.btn_view_all_by_column_name(column_name), doc=name)
            else:
                self.wait_element_visible(Discover.btn_view_all, doc=name)
                self.click_element(Discover.btn_view_all, doc=name)
        else:
            self.wait_element_visible(Discover.btn_view_all, doc=name)
            self.click_element(Discover.btn_view_all, doc=name)

    # 判断是否进入了view all页
    def is_view_all_exist(self):
        """
        :return: True or False
        """
        name = "判断书城的view all是否存在"
        if self.is_element_visible(Discover.btn_search_in_view_all, doc=name):
            return True
        else:
            return False

    # 在书城点击搜索
    def click_search(self):
        name = "在书城页面点击搜索框"
        self.wait_element_visible(Discover.btn_search, doc=name)
        self.click_element(Discover.btn_search, doc=name)

    # 判断书城的搜索页是否存在
    def is_search_exist(self):
        """
        :return: True or False
        """
        name = "判断书城的搜索页是否存在"
        if self.is_element_visible(Discover.btn_cancel, doc=name):
            return True
        else:
            return False

    # 点击搜索页面的取消按钮
    def click_cancel_in_search(self):
        name = "点击搜索页面的取消按钮"
        self.wait_element_visible(Discover.btn_cancel, doc=name)
        self.click_element(Discover.btn_cancel, doc=name)

    # 在书城点击打赏榜单
    def click_top_of_list(self):
        name = "在书城页面点击打赏榜单"
        self.wait_element_visible(Discover.btn_list, doc=name)
        self.click_element(Discover.btn_list, doc=name)

    # 在书城点击延时解锁
    def click_delay_unlock(self):
        name = "在书城页面点击延时解锁"
        self.wait_element_visible(Discover.btn_delay, doc=name)
        self.click_element(Discover.btn_delay, doc=name)

    # 判断延时解锁页面是否存在
    def is_delay_unlock_exist(self):
        """
        :return: True or False
        """
        name = "判断延时解锁页面是否存在"
        if self.is_element_visible(Discover.btn_delay_unlock_today, doc=name):
            return True
        else:
            return False

    # 点击延时解锁页面的返回
    def click_back(self):
        name = "点击延时解锁页面的返回按钮"
        self.wait_element_visible(Discover.btn_back, doc=name)
        self.click_element(Discover.btn_back, doc=name)

    # 在书城点击消息通知
    def click_inbox_in_discover(self):
        name = "在书城页面点击消息通知"
        self.wait_element_visible(Discover.btn_inbox, doc=name)
        self.click_element(Discover.btn_inbox, doc=name)

    # 点击banner(待完善)
    def click_banner(self, index=None):
        """
        先判断是否存在banner,如果不存在则报错;
        如果存在则判断是否有Index,根据index数量向左滑动多少次;
        否则点击展示出来的默认banner
        :param index:banner的页数
        :return:
        """
        name = "在书城页面点击banner"
        try:
            if self.is_element_visible(Discover.btn_banner, doc=name):
                if index is not None:
                    num = self.get_elements(Discover.num_of_banner, doc=name)
                    for i in range(num):
                        # 在banner中滑屏的次数(待完善基础操作中手机滑屏相关操作)
                        pass
                self.click_element(Discover.btn_banner, doc=name)
        except Exception as e:
            log.error("场景中不存在banner")
            raise e
