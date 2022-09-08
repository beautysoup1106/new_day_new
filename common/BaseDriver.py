from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from config.setting import *
import allure

'''基础操作类'''


class BaseDriver:

    def __init__(self, driver):
        self.driver = driver

    # 查找元素(判断元素是否在当前页面出现)
    def find_element(self, el):
        """
        param el: 需要查找元素的名称(el是element的缩写)
        return: True or False
        """
        source = self.driver.page_source
        if el in source:
            return True
        else:
            log.info('找不到页面元素{}'.format(el))
            return False

    # 等待元素可见
    def wait_element_visible(self, locator, doc='', times=30, poll_frequency=0.5):
        """
        param locator: 元素定位
        param doc: 操作的模块名_页面名_操作名(用于异常时截图存储的截图图片名称)
        param time: 等待时间
        param poll_frequency: 轮询间隔时间
        return:
        """
        try:
            log.info('等待元素{}可见'.format(locator))
            start_time = datetime.now()
            WebDriverWait(self.driver, times, poll_frequency).until(expected_conditions.
                                                                    visibility_of_element_located(locator))
        except Exception as e:
            log.info('等待元素{}失败'.format(locator))
            self.save_screenshots(doc)
            raise e

        end_time = datetime.now()
        wait_time = (end_time - start_time).seconds
        log.info('wait_time:{}'.format(wait_time))
        log.info('等待结束,等待时长为{}秒'.format(wait_time))

    # 截图
    def save_screenshots(self, doc=''):
        """
        param doc: 操作的模块名_页面名_操作名(用于异常时截图存储的截图图片名称)
        return:
        """
        log.info('截取屏幕')
        file_name = joinPath(screenshot_dir, '{}_{}.png'.format(datetime.now().strftime('%Y%m%d%H%M%S'), doc))
        self.driver.save_screenshot(file_name)
        with open(file_name, mode='rb') as f:
            file = f.read()
        allure.attach(file, doc, allure.attachment_type.PNG)
        log.info('截图完成,存放地址在{}'.format(file_name))

    # 判断元素是否存在
    def is_element_visible(self, locator, doc='', times=10, poll_frequency=0.5):
        """
        param locator: 元素定位
        param doc: 操作的模块名_页面名_操作名(用于异常时截图存储的截图图片名称)
        param time: 等待时间
        param poll_frequency: 轮询间隔时间
        return:
        """
        try:
            log.info('等待元素{}可见'.format(locator))
            WebDriverWait(self.driver, times, poll_frequency).until(expected_conditions.
                                                                    presence_of_all_elements_located(locator))
            return True
        except Exception as e:
            self.save_screenshots(doc)
            log.info(e)
            return False

    # 找到元素
    def get_element(self, locator, doc=''):
        """
        :param doc: 操作的模块名_页面名_操作名(用于异常时截图存储的截图图片名称)
        :param locator: 元素定位
        :return:
        """
        log.info('查找元素{}'.format(locator))
        try:
            ele = self.driver.find_element(*locator)
            return ele
        except Exception as e:
            log.info('查找元素{}失败'.format(locator))
            self.save_screenshots(doc)
            raise e

    # 找到元素集
    def get_elements(self, locator, doc=''):
        """
        :param locator: 元素定位
        :param doc:
        :return: nums
        """
        log.info('查找元素{}'.format(locator))
        try:
            ele = self.driver.find_elements(*locator)
            return len(ele)
        except Exception as e:
            log.info('查找元素{}失败'.format(locator))
            self.save_screenshots(doc)
            raise e

    # 输入内容
    def input_text(self, locator, text, doc=''):
        """
        param locator: 元素定位
        param text: 输入的内容
        param doc: 操作的模块名_页面名_操作名(用于异常时截图存储的截图图片名称)
        return:
        """
        ele = self.get_element(locator, doc)
        log.info('在元素{}处输入内容{}'.format(locator, text))
        try:
            ele.send_keys(text)
        except Exception as e:
            log.info('在元素{}处输入内容{}失败'.format(locator, text))
            self.save_screenshots(doc)
            raise e

    # 点击元素
    def click_element(self, locator, doc=''):
        """
        param locator: 元素定位
        param doc: 操作的模块名_页面名_操作名(用于异常时截图存储的截图图片名称)
        return:
        """
        ele = self.get_element(locator, doc)
        log.info('在元素{}处点击'.format(locator))
        try:
            ele.click()
        except Exception as e:
            log.info('在元素{}处点击失败'.format(locator))
            self.save_screenshots(doc)
            raise e

    # 获取文本
    def get_text(self, locator, doc=''):
        """
        param locator: 元素定位
        param doc: 操作的模块名_页面名_操作名(用于异常时截图存储的截图图片名称)
        return: text
        """
        ele = self.get_element(locator, doc)
        log.info('获取元素{}的文本'.format(locator))
        try:
            return ele.text
        except Exception as e:
            log.info('获取元素{}的文本失败'.format(locator))
            self.save_screenshots(doc)
            raise e

    # 清空输入框内容
    def clear_text(self, locator, doc=''):
        """
        param locator: 元素定位
        param doc: 操作的模块名_页面名_操作名(用于异常时截图存储的截图图片名称)
        return:
        """
        ele = self.get_element(locator, doc)
        log.info('清空输入框{}的内容'.format(locator))
        try:
            ele.clear()
        except Exception as e:
            log.info('清空输入框{}的内容失败'.format(locator))
            self.save_screenshots(doc)
            raise e

    # 获取元素属性
    def get_attribute(self, locator, attr, doc=''):
        """
        param locator: 元素定位
        param attr: 属性名称
        param doc: 操作的模块名_页面名_操作名(用于异常时截图存储的截图图片名称)
        return:
        """
        ele = self.get_element(locator, doc)
        log.info('获取元素{}的文本'.format(locator))
        try:
            return ele.get_attribute(attr)
        except Exception as e:
            log.info('获取元素{}的属性失败'.format(locator))
            self.save_screenshots(doc)
            raise e

    # 弹窗处理-同意
    def accept_alert(self, times=5, poll_frequency=0.5, doc=''):
        """
        param times: 等待时长,默认30秒
        param poll_frequency: 频率，默认0.5秒获取一次
        param doc: 操作的模块名_页面名_操作名(用于异常时截图存储的截图图片名称)
        return:
        """
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(expected_conditions.alert_is_present())
            alert = self.driver.switch_to_alert()
            alert.accept()
        except Exception as e:
            log.info('弹窗不存在')
            self.save_screenshots(doc)
            raise e

    # 弹窗处理-取消
    def dismiss_alert(self, times=5, poll_frequency=0.5, doc=''):
        """
        param times: 等待时长,默认30秒
        param poll_frequency: 频率，默认0.5秒获取一次
        param doc: 操作的模块名_页面名_操作名(用于异常时截图存储的截图图片名称)
        return:
        """
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(expected_conditions.alert_is_present())
            alert = self.driver.switch_to_alert()
            alert.dismiss()
        except Exception as e:
            log.info('弹窗不存在')
            self.save_screenshots(doc)
            raise e

    # 弹窗处理-获取弹窗内容
    def get_text_in_alert(self, times=5, poll_frequency=0.5, doc=''):
        """
        param times: 等待时长,默认30秒
        param poll_frequency: 频率，默认0.5秒获取一次
        param doc: 操作的模块名_页面名_操作名(用于异常时截图存储的截图图片名称)
        return: alert.text，返回弹窗中文本内容
        """
        try:
            WebDriverWait(self.driver, times, poll_frequency).until(expected_conditions.alert_is_present())
            alert = self.driver.switch_to_alert()
            return alert.text
        except Exception as e:
            log.info('弹窗不存在')
            self.save_screenshots(doc)
            raise e

    # 按压屏幕
    def press_screen(self, locator=None, x=100, y=100, doc=''):
        """
        按压屏幕
        :param locator:元素定位
        :param x:X轴坐标
        :param y:Y轴坐标
        :param doc:操作的模块名_页面名_操作名(用于异常时截图存储的截图图片名称)
        :return:
        """
        if locator is not None:
            ele = self.get_element(locator, doc)
            log.info('在元素{}处按压'.format(ele))
            try:
                TouchAction(self.driver).press(el=ele).release().perform()
            except Exception as e:
                log.info('在元素{}处按压失败'.format(ele))
                self.save_screenshots(doc)
                raise e
        else:
            log.info('在坐标X=100,Y=100处按压')
            try:
                TouchAction(self.driver).press(x=x, y=y).release().perform()
            except Exception as e:
                log.info('在坐标X=100,Y=100处按压失败')
                self.save_screenshots(doc)
                raise e

    # 手机键盘缩回
    def sys_hide_keyboard(self):
        self.driver.hide_keyboard()

    # 手机键盘 返回
    def sys_back(self):
        self.driver.back()

    def sliding_screen(self, direction, doc=''):
        """
        滑屏操作
        :param direction: 滑屏方向：上-up;下-down;左-left;右-right
        :param doc: 操作的模块名_页面名_操作名(用于异常时截图存储的截图图片名称)
        :return:
        """
        size = self.driver.get_window_size()
        try:
            log.info("开始向{}方向滑动".format(direction))
            if direction.lower() == 'up':
                self.driver.swipe(start_x=size['width'] * 0.5,
                                  start_y=size['height'] * 0.9,
                                  end_x=size['width'] * 0.5,
                                  end_y=size['height'] * 0.1,
                                  duration=200)
            elif direction.lower() == 'down':
                self.driver.swipe(start_x=size['width'] * 0.5,
                                  start_y=size['height'] * 0.1,
                                  end_x=size['width'] * 0.5,
                                  end_y=size['height'] * 0.9,
                                  duration=200)
            elif direction.lower() == 'left':
                self.driver.swipe(start_x=size['width'] * 0.9,
                                  start_y=size['height'] * 0.5,
                                  end_x=size['width'] * 0.1,
                                  end_y=size['height'] * 0.5,
                                  duration=200)
            elif direction.lower() == 'right':
                self.driver.swipe(start_x=size['width'] * 0.1,
                                  start_y=size['height'] * 0.5,
                                  end_x=size['width'] * 0.9,
                                  end_y=size['height'] * 0.5,
                                  duration=200)
            else:
                log.error("方向选择错误！")
        except Exception as e:
            log.error("向{}方向滑动屏幕失败！".format(direction))
            self.save_screenshots(doc)
            raise e

    # 获取toast提示信息
    # automationName: UiAutomator2  这样设置caps才能处理toast
    def get_toastMsg(self, toast, doc=''):
        # 1、xpath表达式，文本匹配
        loc = (MobileBy.XPATH, '//*[contains(@text,"{}")]'.format(toast))
        # 等待室等待元素存在，不能用等待元素可见
        try:
            WebDriverWait(self.driver, 10, 0.01).until(expected_conditions.visibility_of_element_located(loc))
            return self.driver.find_element(*loc).text
        except Exception as e:
            log.error('没有找到匹配的toast！！！')
            self.save_screenshots(doc)
            raise e

if __name__ == '__main__':
    container=BaseDriver()
