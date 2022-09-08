import os
import sys
from common.logger import Logger
from common import init_global_var
BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)

ENV = init_global_var.get_value(key='env', defvalue='test')

EMAIL_INFO = {
    'user': 'guojianfeng@stary.ltd',
    'host': 'smtp.exmail.qq.com',
    'password': 'Gjfsl1314'
}

TO = ['guojianfeng@stary.com']

CC = []

Webhook = 'https://oapi.dingtalk.com/robot/send?access_token=e5822464bd4d4d323f1007ef0759e5b2cad70ecc6ff2dd2ccb46d06' \
          '7382c300e'

LOG_LEVEL = 'debug'

CASE_PATH = os.path.join(BASE_PATH, 'testcases')  # 查找用例的目录

SRC_PATH = os.path.join(BASE_PATH, 'product/')

LOG_PATH = os.path.join(BASE_PATH, 'logs', 'test.log')

REPORT_PATH = os.path.join(BASE_PATH, 'report')

CASE_FILE_START = 'test'  # 这个找用例的规则，以什么开头就运行

# 日志路径
LOG_PATH = os.path.join(BASE_PATH, 'logs', 'test.log')

log = Logger(file_name=LOG_PATH, level=LOG_LEVEL)

#生产yaml文件路径
HAR_PATH = os.path.join(BASE_PATH, 'harfile')

# 截图路径
screenshot_dir = os.path.join(BASE_PATH, 'Screenshots')

# 连接路径函数
joinPath = lambda a, *b: os.path.join(a, *b)

# 设备配置文件
yaml_dir = os.path.join(BASE_PATH, "config", "yaml-appium.yaml")

# appPackage配置文件
appPackage_dir = os.path.join(BASE_PATH, "config", "appPackage.yaml")

if __name__ == '__main__':
    log.debug('debug信信息')
