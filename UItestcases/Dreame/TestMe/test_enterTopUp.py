# -*- coding: utf-8 -*-
"""
@File: test_enterTopUp.py
@Author: peterpang
@Time: 2021/10/27 11:24
"""
import pytest
from PageObject.MePage.topup_page import Topup
from PageObject.MePage.Login_page import Login
from config.setting import log


@pytest.mark.usefixtures("is_logined")
class TestTopUp:

    # 进入商店
    def test_enter_topup(self, is_logined):
        log.info("开始执行测试用例test_enter_topup")
        # 点击me页面
        Login(is_logined).click_Me()
        # 点击商店页面
        Topup(is_logined).click_topup()
        # 断言,判断已进入商店页面
        assert Topup(is_logined).is_topup_page_exist() == True
        # 返回上一层
        Topup(is_logined).click_back()
        log.info("完成测试用例test_enter_topup")


if __name__ == '__main__':
    pytest.main(["-s", f"{__file__}::TestTopUp"])
