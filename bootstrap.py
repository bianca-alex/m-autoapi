# coding=utf-8
import pytest
import sys
from utils.loader_config import config

class BootStrap:
    @classmethod
    def run(cls, report_engine='html'):
        # 获取是否生成报告的配置
        generate_report = config.get("report") == 'True'

        # 初始化默认参数
        argv = ['./tests/']
        report_path = './reports/all/'

        # 检查是否启用重试机制
        try_flag = config.get("try_flag")
        if try_flag == 'True':
            try_num = int(config.get("try_num", "Unit"))
            try_time = int(config.get("try_time", "Unit"))

            # 配置 pytest 命令行选项以包括重试次数和重试间隔
            argv.extend(['--reruns', str(try_num), '--reruns-delay', str(try_time)])

        if len(sys.argv) == 2:
            module_name = sys.argv[1]
            argv = ['./tests/' + module_name + '/']
            report_path = f'./reports/{module_name}/'

        if len(sys.argv) == 3:
            module_name, file_name = sys.argv[1], sys.argv[2]
            argv = ['./tests/' + module_name + '/' + file_name + '.py']
            report_path = f'./reports/{module_name}_{file_name}/'

        # 生成报告参数
        if report_engine == 'html':
            report_option = ['--html=' + report_path + 'index.html'] if generate_report else []
        elif report_engine == 'allure':
            report_option = ['--alluredir=' + report_path] if generate_report else []
        else:
            sys.exit("未支持的报告引擎！！！")
        
        # 执行测试用例
        pytest.main(argv + report_option)

# 在其他地方调用 BootStrap.run() 即可执行测试用例，并根据配置生成报告和应用重试机制。
