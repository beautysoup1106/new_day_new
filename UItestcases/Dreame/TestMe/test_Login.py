# -*- coding: utf-8 -*-
"""
@File: test_Login.py
@Author: peterpang
@Time: 2021/10/27 14:26
"""
import pytest
from PageObject.MePage.Login_page import Login
from config.setting import log


@pytest.mark.usefixtures("is_logined")
class TestLogin:

    # 邮箱登录
    def test_login_by_email(self, is_logined):
        log.info("开始执行测试用例test_login_by_email")
        # 点击me页面
        Login(is_logined).click_Me()
        # 点击username
        Login(is_logined).click_username()
        # 邮箱登录
        Login(is_logined).login_by_email("tpwebx73062@chacuo.net", "123456")
        # 点击me页面
        Login(is_logined).click_Me()
        # 断言,判断已经登录
        assert Login(is_logined).get_username() == "tpwebx73062"
        # 退出登录
        Login(is_logined).logout()
        log.info("完成测试用例test_login_by_email")

    # facebook登录
    def test_login_by_facebook(self, is_logined):
        log.info("开始执行测试用例test_login_by_facebook")
        # 点击me页面
        Login(is_logined).click_Me()
        # 点击username
        Login(is_logined).click_username()
        # 邮箱登录
        Login(is_logined).login_by_facebook()
        # 点击me页面
        Login(is_logined).click_Me()
        # 断言,判断已经登录
        assert Login(is_logined).get_username() == "Mamba Zhang"
        # 退出登录
        Login(is_logined).logout()
        log.info("完成测试用例test_login_by_facebook")

    # 谷歌账号登录
    def test_login_by_google(self, is_logined):
        log.info("开始执行测试用例test_login_by_google")
        # 点击me页面
        Login(is_logined).click_Me()
        # 点击username
        Login(is_logined).click_username()
        # 邮箱登录
        Login(is_logined).login_by_google()
        # 点击me页面
        Login(is_logined).click_Me()
        # 断言,判断已经登录
        assert Login(is_logined).get_username() == "Peng ting"
        # 退出登录
        Login(is_logined).logout()
        log.info("完成测试用例test_login_by_google")


if __name__ == '__main__':
    pytest.main(["-s", f"{__file__}::TestLogin::test_login_by_google"])
