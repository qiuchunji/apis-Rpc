import os
import shutil
import pytest
from config import Conf
from common.Base import allure_report
from common.Base import send_mail


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    :param filepath: 路径
    :return:
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


if __name__ == '__main__':
    try:
        del_file(Conf.get_report_path()+os.sep+"result")
        del_file(Conf.get_report_path()+os.sep+"html")
    except Exception as e:
        print(e)
    report_path = Conf.get_report_path()+os.sep+"result"
    report_html_path = Conf.get_report_path()+os.sep+"html"
    pytest.main(["-s","--alluredir", report_path])
    allure_report(report_path, report_html_path)
