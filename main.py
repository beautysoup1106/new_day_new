import sys, os, time, shutil, subprocess

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_PATH)

import urllib3

urllib3.disable_warnings()
import pytest
from config.setting import REPORT_PATH, SRC_PATH
from common.tools import send_mail, dingtalk
from common import init_global_var
if __name__ == '__main__':
    '''env参数控制是测试环境还是非测试环境,测试环境可以指定T几环境，格式字符串与test逗号分隔'''
    env = 'release,t3'
    init_global_var.set_value('env', env)
    t = time.strftime('%Y%m%d%H%M%S')
    result_path = os.path.join(REPORT_PATH, 'xml')
    report_path = os.path.join(REPORT_PATH, 'html')
    try:
        shutil.rmtree(result_path)
    except Exception as e:
        pass
    mark = 'all'
    num = '0'
    reruns = '1'
    status = pytest.main(['-q', '-s', SRC_PATH, '-m', mark,'--alluredir', result_path])
    env_file = os.path.join(result_path, 'environment.properties')
    with open(env_file, 'w+') as f:
        domain = "https://api.t1.dreame.com"
        f.write('Domain={}'.format(domain))
    command = "allure generate  %s -o %s --clean" % (result_path, report_path)
    subprocess.call(command, shell=True)
    # if status !=0 :
    #     send_mail()
    #     dingtalk()
