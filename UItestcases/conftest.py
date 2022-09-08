import pytest
import yaml
from config.setting import *
from appium import webdriver
from PageObject.MePage.Login_page import Login


def get_desired_caps(platformName='Android', devices_name='vivo1906', appName='Dreame', port=4723):
    """
    :return: desired_caps, 返回appium配置信息
    :return: port, 返回端口号
    """
    # 根据devices_name获取deviceName值
    with open(yaml_dir, "r", encoding="utf-8") as fs:
        deviceName = yaml.load(fs, Loader=yaml.FullLoader)
        deviceName = deviceName[devices_name]
    # 根据appName获取appPackage中的appPackage值
    with open(appPackage_dir, "r", encoding="utf-8") as fs:
        appPackage = yaml.load(fs, Loader=yaml.FullLoader)
        appPackage = appPackage[appName]
    desired_caps = {
        'platformName': platformName,
        'deviceName': deviceName,
        'appPackage': appPackage,
        'noReset': True,
        'platformVersion': '11',
        'appActivity': appPackage + '.ui.MainActivity',
        'newCommandTimeout': 120
    }
    return desired_caps, port


# 启动会话设置noReset=True,启动设置(基于已经设置好的APP环境及登录账号上进行测试)
@pytest.fixture(scope="class")
def is_logined():
    desired_caps = get_desired_caps()[0]
    port = get_desired_caps()[1]
    driver = webdriver.Remote("http://localhost:" + str(port) + "/wd/hub", desired_capabilities=desired_caps)
    # 打开APP后判断是否弹出推广,如果是则关闭,如果否则不理会
    Login(driver).close_user_guide()
    # 判断是否已经登录待写
    Login(driver).click_LoggerOpened()
    yield driver


# 启动会话设置noReset=False,启动设置
@pytest.fixture(scope="class")
def base_driver(noReset=False):
    with open(yaml_dir, "r", encoding="utf-8") as fs:
        desired_caps = yaml.load(fs, Loader=yaml.FullLoader)
        desired_caps = desired_caps[devices_name]
        # desired_caps = desired_caps[devices_name]["desired_caps"]
        desired_caps["noReset"] = noReset
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities=desired_caps)
        # 打开APP后判断是否弹出推广,如果是则关闭,如果否则不理会
        Login(driver).close_user_guide()
        # 暂时不用,待完善重启APP后需要做的判断
        yield driver
