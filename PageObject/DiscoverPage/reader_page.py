# -*- coding: utf-8 -*-
"""
@File: reader_page.py
@Author: peterpang
@Time: 2021/10/29 9:25
"""
import time
from common.BaseDriver import BaseDriver
from PageLocators.Locators_Discover import Discover


class ReaderPage(BaseDriver):
    """阅读器相关操作"""

    # 点击书籍详情页的start reading
    def click_start_read(self):
        name = "在书籍详情页点击开始阅读"
        if self.is_element_visible(Discover.author_name_in_detail_page, doc=name):
            self.wait_element_visible(Discover.btn_start_read, doc=name)
            self.click_element(Discover.btn_start_read, doc=name)

    # 判断是否进入了阅读器
    def is_reader_page_exist(self):
        """
        :return: True or False
        """
        name = "判断是否进入了阅读器"
        if self.is_element_visible(Discover.content_in_reader, doc=name):
            return True
        else:
            return False

    # 判断是否进入书籍详情页
    def is_book_detail_page_exist(self):
        """
        :return: True or False
        """
        name = "判断是否进入书籍详情页"
        if self.is_element_visible(Discover.btn_start_read, doc=name):
            return True
        else:
            return False

    # 点击书籍详情页的下载页(在阅读器点击下载页)
    def click_download_in_book_detail_page(self):
        name = "在书籍详情页点击download"
        self.wait_element_visible(Discover.btn_download_in_detail_page, doc=name)
        self.click_element(Discover.btn_download_in_detail_page, doc=name)

    # 判断是否进入下载页面
    def is_download_page_exist(self):
        """
        :return: True or False
        """
        name = "判断是否进入下载页面"
        if self.is_element_visible(Discover.btn_close_in_download, doc=name):
            return True
        else:
            return False

    # 关闭下载页面
    def click_close_in_download_page(self):
        name = "在下载页面点击关闭"
        self.wait_element_visible(Discover.btn_close_in_download, doc=name)
        self.click_element(Discover.btn_close_in_download, doc=name)

    # 获取书籍详情页下载按钮旁的标签,是OFF还是FREE
    def get_tag_from_download_in_download_page(self):
        """
        :return: tag, OFF还是FREE
        """
        name = "获取书籍详情页下载按钮旁的标签"
        self.wait_element_visible(Discover.tag_from_download_in_detail_page, doc=name)
        tag = self.get_text(Discover.tag_from_download_in_detail_page, doc=name)
        return tag

    # 判断书籍详情页下载按钮旁的标签是否存在(当书籍被删除时则不存在)
    def is_tag_from_download_exist(self):
        """
        :return: True or False
        """
        name = "判断是否进入下载页面"
        if self.is_element_visible(Discover.tag_from_download_in_detail_page, doc=name):
            return True
        else:
            return False

    # 点击书籍详情页的report
    def click_report_in_book_detail_page(self):
        name = "在书籍详情页点击report"
        self.wait_element_visible(Discover.btn_more_in_detail_page, doc=name)
        self.click_element(Discover.btn_more_in_detail_page, doc=name)
        self.wait_element_visible(Discover.btn_report, doc=name)
        self.click_element(Discover.btn_report, doc=name)

    # 点击书籍详情页的share
    def click_share_in_book_detail_page(self):
        name = "在书籍详情页点击share"
        self.wait_element_visible(Discover.btn_more_in_detail_page, doc=name)
        self.click_element(Discover.btn_more_in_detail_page, doc=name)
        self.wait_element_visible(Discover.btn_share, doc=name)
        self.click_element(Discover.btn_share, doc=name)

    # 判断是否进入分享页面
    def is_share_page_exist(self):
        """
        :return: True or False
        """
        name = "判断是否进入分享页面"
        if self.is_element_visible(Discover.copyLink_in_share, doc=name):
            return True
        else:
            return False

    # 点击书籍详情页的收藏按钮
    def click_follow_in_detail_page(self):
        name = "在书籍详情页点击收藏按钮"
        self.wait_element_visible(Discover.btn_follow_in_detail_page, doc=name)
        self.click_element(Discover.btn_follow_in_detail_page, doc=name)

    # 判断收藏是否成功
    def is_follow_succeed(self):
        """
        :return: True or False
        """
        name = "判断收藏是否成功"
        if self.is_element_visible(Discover.toast_add_library, doc=name):
            return True
        else:
            return False

    # 在阅读器点击屏幕
    def press_reader(self):
        name = "在阅读器点击"
        self.wait_element_visible(Discover.content_in_reader, doc=name)
        self.press_screen(Discover.content_in_reader, doc=name)

    # 点阅读器点击章节
    def click_menu_in_reader(self):
        name = "点阅读器点击章节"
        self.wait_element_visible(Discover.btn_menu_in_reader, doc=name)
        self.press_screen(Discover.btn_menu_in_reader, doc=name)

    # 获取付费章节数
    def get_nums_of_pay_episodes(self):
        """
        :return: 返回当前页面需要付费的章节数
        """
        name = "获取付费章节数"
        self.wait_element_visible(Discover.lock_icon_in_episodes, doc=name)
        nums = self.get_elements(Discover.lock_icon_in_episodes, doc=name)
        return nums

    # 点击付费章节
    def click_pay_episodes(self, i):
        name = "点击付费章节"
        self.wait_element_visible(Discover.lock_icon_in_episodes, doc=name)
        self.click_element(Discover.btn_episodes_from_unlock(i))

    # 判断付费按钮是否存在
    def is_pay_btn_exist(self):
        """
        :return: True or False
        """
        name = "判断付费按钮是否存在"
        if self.is_element_visible(Discover.btn_unlock_in_reader, doc=name):
            return True
        else:
            return False

    # 点击付费按钮
    def click_pay_btn(self):
        name = "点击付费按钮"
        self.wait_element_visible(Discover.btn_unlock_in_reader, doc=name)
        self.click_element(Discover.btn_unlock_in_reader, doc=name)

    # 点击评论按钮
    def click_comment(self):
        name = "点击评论按钮"
        self.wait_element_visible(Discover.btn_comment_in_reader, doc=name)
        self.click_element(Discover.btn_comment_in_reader, doc=name)

    # 输入评论
    def input_content(self, content):
        name = "输入评论"
        self.wait_element_visible(Discover.ipt_content, doc=name)
        self.click_element(Discover.ipt_content, doc=name)
        self.input_text(Discover.ipt_content, content, doc=name)
        time.sleep(1)
        self.click_element(Discover.btn_send_content, doc=name)

    # 获取评论
    def get_content(self):
        """
        :return: content
        """
        name = "获取评论"
        self.wait_element_visible(Discover.content, doc=name)
        content = self.get_text(Discover.content, doc=name)
        return content
