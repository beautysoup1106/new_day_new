# -*- coding: utf-8 -*-
"""
@File: library_page.py
@Author: peterpang
@Time: 2021/11/23 15:04
"""
from common.BaseDriver import BaseDriver
from PageLocators.Locators_Library import Library


class LibraryPage(BaseDriver):
    """书架相关操作"""

    # 点击书架模块
    def click_library(self):
        name = "点击书架模块"
        self.wait_element_visible(Library.btn_library, doc=name)
        self.click_element(Library.btn_library, doc=name)

    # 点击任务中心
    def click_task_center(self):
        name = "点击任务中心"
        self.wait_element_visible(Library.btn_task_in_library, doc=name)
        self.click_element(Library.btn_task_in_library, doc=name)

    # 点击延时解锁
    def click_delay(self):
        name = "点击延时解锁"
        self.wait_element_visible(Library.btn_delay_in_library, doc=name)
        self.click_element(Library.btn_delay_in_library, doc=name)

    # 点击inbox
    def click_inbox_in_library(self):
        name = "点击inbox"
        self.wait_element_visible(Library.btn_inbox_in_library, doc=name)
        self.click_element(Library.btn_inbox_in_library, doc=name)

    # 点击download
    def click_download_in_library(self):
        name = "点击download"
        self.wait_element_visible(Library.btn_more_in_library, doc=name)
        self.click_element(Library.btn_more_in_library, doc=name)
        self.wait_element_visible(Library.btn_download_in_library, doc=name)
        self.click_element(Library.btn_download_in_library, doc=name)

    # 点击viewed
    def click_viewed_in_library(self):
        name = "点击viewed"
        self.wait_element_visible(Library.btn_more_in_library, doc=name)
        self.click_element(Library.btn_more_in_library, doc=name)
        self.wait_element_visible(Library.btn_viewed_in_library, doc=name)
        self.click_element(Library.btn_viewed_in_library, doc=name)

    # 点击Edit library
    def click_edit_library(self):
        name = "点击Edit library"
        self.wait_element_visible(Library.btn_more_in_library, doc=name)
        self.click_element(Library.btn_more_in_library, doc=name)
        self.wait_element_visible(Library.btn_edit_in_library, doc=name)
        self.click_element(Library.btn_edit_in_library, doc=name)

    # 点击关闭more窗口
    def click_close_at_more(self):
        name = "点击关闭more窗口"
        self.wait_element_visible(Library.btn_close_in_library, doc=name)
        self.click_element(Library.btn_close_in_library, doc=name)

    # 点击书架的第一本书籍
    def click_book_in_library(self):
        name = "点击书架的第一本书籍"
        self.wait_element_visible(Library.btn_following_book_in_library, doc=name)
        self.click_element(Library.btn_following_book_in_library, doc=name)
