# -*- coding: utf-8 -*-
"""
@File: Login_page.py
@Author: peterpang
@Time: 2021/10/22 11:38
"""
from PageLocators.Locators_Me import Me
from common.BaseDriver import BaseDriver
from PageLocators.Locators_Library import Library


class Login(BaseDriver):

    # 关闭启动APP时的环境日志启动提醒
    def click_LoggerOpened(self):
        name = "关闭启动APP时的环境日志启动提醒"
        if self.is_element_visible(Library.close_set, doc=name):
            self.wait_element_visible(Library.close_set, doc=name)
            self.click_element(Library.close_set, doc=name)

    # 关闭进入App后的推广弹窗
    def close_user_guide(self):
        name = "关闭进入App后的推广"
        if self.is_element_visible(Me.btn_logout_cancel, times=5):
            self.wait_element_visible(Me.btn_logout_cancel, doc=name)
            self.click_element(Me.btn_logout_cancel, doc=name)

    # 进入Me页面
    def click_Me(self):
        name = "进入Me页面"
        self.wait_element_visible(Me.btn_Me, doc=name)
        self.click_element(Me.btn_Me, doc=name)

    # 点击用户头像
    def click_user_image(self):
        name = "点击用户头像"
        self.wait_element_visible(Me.btn_image, doc=name)
        self.click_element(Me.btn_image, doc=name)

    # 点击用户姓名
    def click_username(self):
        name = "点击第三方登录按钮"
        self.wait_element_visible(Me.btn_username, doc=name)
        self.click_element(Me.btn_username, doc=name)

    # 点击第三方登录按钮
    def third_party_login(self):
        name = "点击第三方登录按钮"
        self.wait_element_visible(Me.btn_third_party_login, doc=name)
        self.click_element(Me.btn_third_party_login, doc=name)

    # 邮箱登录
    def login_by_email(self, email_acc, email_pwd):
        """
        :param email_acc: 邮箱账号
        :param email_pwd: 邮箱密码
        :return:
        """
        name = "邮箱登录"
        self.wait_element_visible(Me.btn_email, doc=name)
        self.click_element(Me.btn_email, doc=name)
        self.wait_element_visible(Me.ipt_email_acc, doc=name)
        self.input_text(Me.ipt_email_acc, email_acc, doc=name)
        self.input_text(Me.ipt_email_pwd, email_pwd, doc=name)
        self.click_element(Me.btn_email_login, doc=name)

    # 获取用户名
    def get_username(self):
        """
        :return: username
        """
        name = "获取用户名"
        self.wait_element_visible(Me.btn_username, doc=name)
        username = self.get_text(Me.btn_username, doc=name)
        return username

    # facebook登录
    def login_by_facebook(self):
        name = "facebook账号登录"
        self.wait_element_visible(Me.btn_facebook, doc=name)
        self.click_element(Me.btn_facebook, doc=name)

    # 谷歌账号登录
    def login_by_google(self):
        name = "谷歌账号登录"
        self.wait_element_visible(Me.btn_google, doc=name)
        self.click_element(Me.btn_google, doc=name)
        # 等待3秒判断是否弹出选择谷歌账号页面
        if self.is_element_visible(Me.btn_google_acc, times=3, doc=name):
            self.click_element(Me.btn_google_acc, doc=name)

    # 退出登录
    def logout(self):
        name = "退出登录操作"
        # 点击setting
        self.wait_element_visible(Me.btn_setting, doc=name)
        self.click_element(Me.btn_setting, doc=name)
        # 点击logout按钮
        self.wait_element_visible(Me.btn_logout, doc=name)
        self.click_element(Me.btn_logout, doc=name)
        # 点击二次确认框的logout按钮
        self.wait_element_visible(Me.btn_logout_confirm, doc=name)
        self.click_element(Me.btn_logout_confirm, doc=name)
        # 点击退出登录后的skip按钮
        self.wait_element_visible(Me.btn_skip, doc=name)
        self.click_element(Me.btn_skip, doc=name)
