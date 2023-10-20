# coding=utf-8
import os

# 获取文件的绝对路径
abs_path = os.path.abspath(__file__)

# 获取文件所在目录的上一级目录,也就是根目录
project_path = os.path.dirname(os.path.dirname(abs_path))

# 通过os.sep的方法来获取config目录的全路径
_conf_path = project_path + os.sep + "config"

# 通过os.sep的方法来获取log日志目录的全路径
_log_path = project_path + os.sep + "logs"

# 通过os.sep的方法来获取report报告目录的全路径
_report_path = project_path + os.sep + "reports"

_data_path = project_path + os.sep + "datas"

_runtime_path = project_path + os.sep + "runtime"


# 返回日志目录
def get_log_path():
    return _log_path

# 返回报告目录
def get_report_path():
    return _report_path

# 返回config目录
def get_config_path():
    return _conf_path

# 返回数据目录
def get_data_path():
    return _data_path

# 返回临时运行目录
def get_runtime_path():
    return _runtime_path

if __name__ == "__main__":
    print(get_log_path())
    print(get_report_path())
    print(get_config_path())
    print(get_data_path())