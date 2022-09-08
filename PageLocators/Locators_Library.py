# -*- coding: utf-8 -*-
"""
@File: Locators_Library.py
@Author: peterpang
@Time: 2021/10/21 10:24
"""
from appium.webdriver.common.mobileby import MobileBy


class Library:
    """Library页面"""
    # 关闭启动时环境提示窗口
    close_set = (MobileBy.ID, "com.dreame.reader:id/snackbar_action")

    # Library
    btn_library = (MobileBy.ID, "//*[@resource-id='com.dreame.reader:id/tabhost_indicator' and @text='Library']")

    # 任务按钮
    btn_task_in_library = (MobileBy.ID, "com.dreame.reader:id/iv_welfare")

    # 延时解锁按钮
    btn_delay_in_library = (MobileBy.ID, "com.dreame.reader:id/iv_time")

    # inbox
    btn_inbox_in_library = (MobileBy.ID, "com.dreame.reader:id/iv_inbox")

    # more
    btn_more_in_library = (MobileBy.ID, "com.dreame.reader:id/more_iv")

    # Downloads
    btn_download_in_library = (MobileBy.ID, "com.dreame.reader:id/download_layout")

    # viewed
    btn_viewed_in_library = (MobileBy.ID, "com.dreame.reader:id/history_layout")

    # Edit Library
    btn_edit_in_library = (MobileBy.ID, "com.dreame.reader:id/edit_iv")

    # 关闭按钮
    btn_close_in_library = (MobileBy.XPATH,
                            "//*[@resource-id='com.dreame.reader:id/close_layout']/android.widget.ImageView")

    # 搜索框
    btn_search_in_library = (MobileBy.ID, "com.dreame.reader:id/tv_search")

    # 搜索输入框
    ipt_search = (MobileBy.ID, "com.dreame.reader:id/et_search_view")

    # 搜索框Novel频道
    search_novel = (MobileBy.XPATH, "//*[@resource-id='com.dreame.reader:id/tab_tv' and @text='Novel']")

    # 搜索框Novel频道
    search_comic = (MobileBy.XPATH, "//*[@resource-id='com.dreame.reader:id/tab_tv' and @text='Comic']")

    # 书架中的第一本书籍(后续可拓展循环,待定)
    btn_following_book_in_library = (MobileBy.ID, "com.dreame.reader:id/following_book_cover")


















