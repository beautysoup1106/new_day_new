# -*- coding: utf-8 -*-
"""
@File: Locators_Me.py
@Author: peterpang
@Time: 2021/10/21 10:26
"""
from appium.webdriver.common.mobileby import MobileBy


class Me:
    """ME界面"""
    # Me模块(未来需要考虑多语言及不同APP时的名称,待优化)
    btn_Me = (MobileBy.XPATH, "//*[@resource-id='com.dreame.reader:id/tabhost_indicator' and @text='Me']")

    # 返回按钮
    btn_back = (MobileBy.ID, "com.dreame.reader:id/icon")

    # 点击用户头像
    btn_image = (MobileBy.ID, "com.dreame.reader:id/user_iv")

    # 点击用户名称
    btn_username = (MobileBy.ID, "com.dreame.reader:id/nick_tv")

    # 进入登录页面(点击提示)
    btn_third_party_login = (MobileBy.ID, "com.dreame.reader:id/visitor_tips")

    # 登录方式选择页面的关闭按钮
    btn_close4loginType = (MobileBy.ID, "com.dreame.reader:id/close_layout")

    # 选择邮箱登录方式
    btn_email = (MobileBy.ID, "com.dreame.reader:id/email_layout")

    # 邮箱账号输入框
    ipt_email_acc = (MobileBy.ID, "com.dreame.reader:id/email_et")

    # 邮箱密码输入框
    ipt_email_pwd = (MobileBy.ID, "com.dreame.reader:id/password_et")

    # 邮箱登录按钮
    btn_email_login = (MobileBy.ID, "com.dreame.reader:id/login_btn")

    # 创建邮箱账号按钮
    btn_create_acc = (MobileBy.ID, "com.dreame.reader:id/sign_tv")

    # 忘记密码按钮
    btn_forgot_pwd = (MobileBy.ID, "com.dreame.reader:id/forget_tv")

    # 选择facebook登录方式
    btn_facebook = (MobileBy.ID, "com.dreame.reader:id/facebook_frameLayout")

    # 选择谷歌登录方式
    btn_google = (MobileBy.ID, "com.dreame.reader:id/google_login_button")

    # 选择谷歌账号
    btn_google_acc = (MobileBy.ID, "com.google.android.gms:id/account_display_name")

    # 商店按钮
    btn_top_up = (MobileBy.ID, "com.dreame.reader:id/store")

    # 商店的第一个支付方式(由于客户端提供的是图片,无法判断支付方式是哪一种,待解决)
    btn_pay_method = (MobileBy.ID, "com.dreame.reader:id/tv_coin")
    print(btn_pay_method)
    # 支付按钮(pay now按钮)--如果选择了officialPay会跳转到浏览器,待解决
    btn_pay_now = (MobileBy.ID, "com.dreame.reader:id/tv_price_pre")

    # 支付页面的金额(获取text后跟支付选择的金额做比较)--整个支付页面的id都一致(需要通过前面的Dreame来拿兄弟节点)
    # balance_pay = (MobileBy.ID, "com.android.vending:id/0_resource_name_obfuscated")

    # 一件购买按钮(待解决,id重复太多)

    # 钱包按钮
    btn_wallet = (MobileBy.ID, "com.dreame.reader:id/wallet")

    # 获取金币余额
    coins_balance = (MobileBy.ID, "com.dreame.reader:id/coin_tv")

    # 交易历史按钮
    trans_his = (MobileBy.ID, "com.dreame.reader:id/recharge_history")

    # 获取标题内容
    title_text = (MobileBy.ID, "com.dreame.reader:id/title_tv")

    # 金券记录
    bonus_rec = (MobileBy.ID, "com.dreame.reader:id/coins_history")

    # 章节解锁记录
    episodes_unl = (MobileBy.ID, "com.dreame.reader:id/purchased_episodes")

    # 章节解锁记录页面的小说频道
    page_episodes_novel = (MobileBy.XPATH, "//*[@resource-id='com.dreame.reader:id/tab_tv' & @text='Novel']")

    # 章节解锁记录页面的漫画频道
    page_episodes_comic = (MobileBy.XPATH, "//*[@resource-id='com.dreame.reader:id/tab_tv' & @text='Comic']")

    # 奖励记录
    reward_rec = (MobileBy.ID, "com.dreame.reader:id/reward_record")

    # 启动自动解锁开关
    turn_on_auto_unl = (MobileBy.XPATH, "//*[@resource-id='com.dreame.reader:id/auto_unlock']"
                                        "/android.widget.RelativeLayout")

    # 任务中心
    btn_task = (MobileBy.ID, "com.dreame.reader:id/task_enter_entrance")

    # 任务中心里的积分记录按钮
    btn_points_record = (MobileBy.XPATH, "//*[@content-desc='POINTS RECORD']/android.widget.Button")

    # 优惠券中心
    btn_coupon = (MobileBy.ID, "com.dreame.reader:id/coupon")

    # 兑换码中心
    btn_redemption_code = (MobileBy.ID, "com.dreame.reader:id/redemption_code")

    # 消息中心
    btn_inbox = (MobileBy.ID, "com.dreame.reader:id/message")

    # 阅读记录
    btn_viewed = (MobileBy.ID, "com.dreame.reader:id/browse_view")

    # following按钮
    btn_following = (MobileBy.ID, "com.dreame.reader:id/follow")

    # 下载中心
    btn_downloads = (MobileBy.ID, "com.dreame.reader:id/download")

    # to be a Dreame Writer!
    btn_writer = (MobileBy.ID, "com.dreame.reader:id/writer")

    # 反馈中心
    btn_feedback = (MobileBy.ID, "com.dreame.reader:id/feedback")

    # 设置中心
    btn_setting = (MobileBy.ID, "com.dreame.reader:id/setting")

    # 退出登录按钮(setting页面下的Logout)
    btn_logout = (MobileBy.ID, "com.dreame.reader:id/me_logout_tv")

    # 弹出框确认按钮
    btn_logout_confirm = (MobileBy.ID, "com.dreame.reader:id/alertRightTV")

    # 弹出框取消按钮
    btn_logout_cancel = (MobileBy.ID, "com.dreame.reader:id/alertLeftTV")

    # 退出登录后的skip按钮
    btn_skip = (MobileBy.ID, "com.dreame.reader:id/skip_tv")
