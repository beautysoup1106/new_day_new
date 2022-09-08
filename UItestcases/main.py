# -*- coding: utf-8 -*-
"""
@File: main.py
@Author: peterpang
@Time: 2022/1/17 9:36
"""


import pytest
import subprocess
import os
from config.setting import REPORT_PATH


if __name__ == '__main__':
    result_path = os.path.join(REPORT_PATH, 'xml')
    report_path = os.path.join(REPORT_PATH, 'html')
    path = 'Dreame/'
    pytest.main(['-s', path, '--alluredir', result_path])
    command = "allure generate  %s -o %s --clean" % (result_path, report_path)
    subprocess.call(command, shell=True)


