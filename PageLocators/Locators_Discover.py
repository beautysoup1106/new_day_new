# -*- coding: utf-8 -*-
"""
@File: Locators_Discover.py
@Author: peterpang
@Time: 2021/10/21 10:26
"""
from appium.webdriver.common.mobileby import MobileBy


class Discover:
    """Discover频道"""
    # Discover模块
    btn_discover = (MobileBy.XPATH, "//*[@resource-id='com.dreame.reader:id/tabhost_indicator' and @text='Discover']")

    # 书城页搜索框
    btn_search = (MobileBy.ID, "com.dreame.reader:id/search_tv")

    # 搜索框的小说频道
    btn_search_novel = (MobileBy.XPATH, "//*[@resource-id='com.dreame.reader:id/tab_tv' & @text='Novel']")

    # 搜索框的小说频道
    btn_search_comic = (MobileBy.XPATH, "//*[@resource-id='com.dreame.reader:id/tab_tv' & @text='Comic']")

    # 搜索框的取消按钮
    btn_cancel = (MobileBy.ID, "com.dreame.reader:id/ll_cancel")

    # 书城页的打赏榜单按钮
    btn_list = (MobileBy.ID, "com.dreame.reader:id/iv_rank")

    # 书城页的延时解锁按钮
    btn_delay = (MobileBy.ID, "com.dreame.reader:id/rl_iv_date")

    # 延时解锁页面的Toady
    btn_delay_unlock_today = (MobileBy.XPATH, "//*[@text='Today']")

    # 延时解锁页面的Tomorrow
    btn_delay_unlock_tomorrow = (MobileBy.XPATH, "//*[@text='Tomorrow']")

    # 延时解锁页面的Unlock按钮
    btn_unlock_in_delayunlockpage = (MobileBy.ID, "com.dreame.reader:id/tv_unlock")

    # 延时解锁页面的返回按钮
    btn_back = (MobileBy.ID, "com.dreame.reader:id/ibtn_return")

    # 书城页的inbox
    btn_inbox = (MobileBy.ID, "com.dreame.reader:id/rl_iv_inbox")

    # 书城页的view all
    @staticmethod
    def btn_view_all_by_column_name(column_name):
        """
        如果提供了栏目名称则点击栏目对应的View all,如果不存在或者没有传则点击第一个view all
        :param column_name:
        :return: loc_view_all， 返回view all所在的XPATH
        """
        loc_view_all = (MobileBy.XPATH,
                        "//*[@resource-id='com.dreame.reader:id/tv_title' & @text='{}']/../../"
                        "android.widget.TextView[@text='View all']".format(column_name))
        return loc_view_all

    # 书城页的第一个view all按钮
    btn_view_all = (MobileBy.XPATH, "//*[@resource-id='com.dreame.reader:id/view_all_tv']/android.widget.TextView")

    # view all页的搜索按钮
    btn_search_in_view_all = (MobileBy.ID, "com.dreame.reader:id/menu_search")

    # 书城页的banner
    btn_banner = (MobileBy.ID, "com.dreame.reader:id/item_iv")

    # 书城页的banner总数
    num_of_banner = (MobileBy.XPATH, "//*[@resource-id='com.dreame.reader:id/view_indicator']/android.widget.ImageView")

    # 根据传入的频道名称返回对应的XPATH
    @staticmethod
    def choose_channel(channel):
        """
        :param channel: 频道名称
        :return: loc_channel, 返回频道名称所在的XPATH
        """
        loc_channel = (MobileBy.XPATH, "//*[@resource-id='com.dreame.reader:id/tab_tv' and @text='{}']".format(channel))
        return loc_channel

    # 点击第一本书
    book_img = (MobileBy.ID, "com.dreame.reader:id/discover_book_cover")

    # 根据传入的书名点击书籍
    @staticmethod
    def choose_book_by_name(book_name):
        """
        :param book_name: 书籍名称
        :return: loc_book, 返回书籍名称所在的XPATH
        """
        loc_book = (MobileBy.XPATH,
                    "//*[@resource-id='com.dreame.reader:id/discover_name' and @text='{}']".format(book_name))
        return loc_book

    # 书籍详情页获取书籍名称
    book_name_in_detail_page = (MobileBy.ID, "com.dreame.reader:id/introduction_book_name")

    # 书籍详情页的下载按钮旁的返回数据,是OFF还是FREE
    tag_from_download_in_detail_page = (MobileBy.ID, "com.dreame.reader:id/iv_free_tag")

    # 书籍详情页的下载按钮(阅读器的下载按钮)
    btn_download_in_detail_page = (MobileBy.ID, "com.dreame.reader:id/download_iv")

    # 书籍详情页下载页面的关闭按钮
    btn_close_in_download = (MobileBy.ID, "com.dreame.reader:id/close_iv")

    # 书籍详情页的更多(阅读器的more)
    btn_more_in_detail_page = (MobileBy.ID, "com.dreame.reader:id/menu_more")

    # 书籍详情页的更多里面的报告按钮
    btn_report = (MobileBy.XPATH, "//*[@resource-id='com.dreame.reader:id/popupTitle' and @text='Report']")

    # 书籍详情页的更多里面的分享按钮
    btn_share = (MobileBy.XPATH, "//*[@resource-id='com.dreame.reader:id/popupTitle' and @text='Share']")

    # 分享页面的书籍名称
    book_name_in_share = (MobileBy.ID, "com.dreame.reader:id/book_name_tv")

    # 分享页面的作者名称
    author_name_in_share = (MobileBy.ID, "com.dreame.reader:id/author_tv")

    # 分享页面的facebook(text=Facebook)
    facebook_in_share = (MobileBy.ID, "com.dreame.reader:id/facebook_tv")

    # 分享页面的instagram(text=Instagram)
    instagram_in_share = (MobileBy.ID, "com.dreame.reader:id/ins_tv")

    # 分享页面的whatsapp(text=WhatsApp)
    whatsapp_in_share = (MobileBy.ID, "com.dreame.reader:id/whats_app_tv")

    # 分享页面的copy link(text=Copy Link)
    copyLink_in_share = (MobileBy.ID, "com.dreame.reader:id/copy_tv")

    # 书籍详情页的作者名称
    author_name_in_detail_page = (MobileBy.ID, "com.dreame.reader:id/introduction_book_author")

    # 书籍详情页的开始阅读按钮
    btn_start_read = (MobileBy.ID, "com.dreame.reader:id/start_read_tv")

    # 书籍详情页的收藏按钮(看不出为收藏与已收藏的区别,待解决)
    btn_follow_in_detail_page = (MobileBy.ID, "com.dreame.reader:id/follow_icon")

    # 书籍详情页的章节总数
    num_of_episodes_in_detail_page = (MobileBy.ID, "com.dreame.reader:id/chapter_num_tv")

    # 书籍详情页的章节按钮
    btn_episodes_in_detail_page = (MobileBy.ID, "com.dreame.reader:id/episodes_tv")

    # 书籍详情页的章节详情的书籍名称
    book_name_in_episodes = (MobileBy.ID, "com.dreame.reader:id/book_name_tv")

    # 书籍详情页的章节详情的章节总数
    num_of_episodes_in_episodes = (MobileBy.ID, "com.dreame.reader:id/num_tv")

    # 书籍详情页的章节详情的锁(获取总的锁数量,轮询总章节数内找到这个锁,进入该章节)--已解锁与未解锁都是该id,无法判断
    lock_icon_in_episodes = (MobileBy.XPATH, "//*[@resource-id='com.dreame.reader:id/status_iv']")

    # 阅读器中的内容
    content_in_reader = (MobileBy.ID, "com.dreame.reader:id/view_content")

    # 阅读器的解锁按钮
    btn_unlock_in_reader = (MobileBy.ID, "com.dreame.reader:id/buy_tv")

    # 阅读器的余额(10 Coins + 0 Bonus,需要正则表达式)
    coins_balance = (MobileBy.ID, "com.dreame.reader:id/coin_desc")

    # 阅读器最上面的章节名称(text=Chapter 10)
    episode_name_in_top = (MobileBy.ID, "com.dreame.reader:id/chapter_name_tv")

    # 阅读器的章节标题(text=Chapter 10)
    episode_title = (MobileBy.ID, "com.dreame.reader:id/title_tv")

    # 阅读器的自动解锁开关(text=Turn on auto-unlock)
    btn_auto_unlock_in_reader = (MobileBy.ID, "com.dreame.reader:id/auto_buy_tv")

    # 阅读器的标题
    title_in_reader = (MobileBy.ID, "com.dreame.reader:id/title_tv")

    # 阅读器的收藏按钮
    btn_follow_in_reader = (MobileBy.ID, "com.dreame.reader:id/follow_icon")

    # 收藏成功的toast
    toast_add_library = (MobileBy.XPATH, "//*[contains(@text, 'You have added this book to your Library.')]")

    # 阅读器内的章节按钮
    btn_menu_in_reader = (MobileBy.ID, "com.dreame.reader:id/menu_iv")

    # 阅读器内章节
    @staticmethod
    def btn_episodes_from_unlock(i):
        """
        :param i: 排序
        :return: XPATH
        """
        return (MobileBy.XPATH, "(//*[@resource-id='com.dreame.reader:id/status_iv'])[{}]"
                                "/preceding-sibling::android.widget.LinearLayout".format(i))

    # 阅读器中的设置按钮
    btn_setting_in_reader = (MobileBy.ID, "com.dreame.reader:id/setting_iv")

    # 阅读器中的阅读模式按钮
    btn_readMode_in_reader = (MobileBy.ID, "com.dreame.reader:id/mode_iv")

    # 阅读器的章节评论按钮
    btn_comment_in_reader = (MobileBy.ID, "com.dreame.reader:id/commet_iv")

    # 阅读器的章节评论数(text=8,判断大于0则点击进入)
    num_comment_in_reader = (MobileBy.ID, "com.dreame.reader:id/comment_count")

    # 阅读器的章节评论中的评论输入框
    ipt_content = (MobileBy.ID, "com.dreame.reader:id/content")

    # 阅读器的章节评论中的评论发送按钮
    btn_send_content = (MobileBy.ID, "com.dreame.reader:id/iv_send")

    # 章节评论的第一条评论
    content = (MobileBy.ID, "com.dreame.reader:id/tv_content")
