from os import read

from appium import webdriver

from androguard.core.bytecodes.apk import APK


def get_apkname(apk):
    a = APK(apk)
    return a.get_package()


def get_main_activity(apk):
    b = APK(apk)
    return b.get_main_activity()

def get_devices():
    cmd="abd devices"
    

# desired_caps = {
#                 'platformName': 'Android',
#                 'deviceName': 'R5CR303RAKE',#adb  deivces
#                 'platformVersion': '11', #从设置中可以获取
#                 'appPackage': get_apkname("./Dreame_v3.8.0_332_0825_dreameapp-23_debug.apk"),#包名
#                 'appActivity': get_main_activity("./Dreame_v3.8.0_332_0825_dreameapp-23_debug.apk"), # apk的launcherActivity
#                 'automationName': 'UiAutomator2',
#                 'skipServerInstallation': True
#                 }
# driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
