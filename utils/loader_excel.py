# -*- coding: utf-8 -*-
import openpyxl
import os
import pytest
from common.settings import get_data_path

# 从Excel文件中读取测试用例数据
def load_test_case(file_path):
    data_path = get_data_path()
    workbook = openpyxl.load_workbook(os.path.join(data_path, file_path))
    sheet = workbook.active
    test_cases = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        test_case = {
            '模块名称': row[0],
            '用例标题': row[1],
            '用例编号': row[2],
            'url': row[3],
            '请求方法': row[4],
            '请求头': row[5],
            'cookies': row[6],
            '请求体': row[7],
            '预期结果': row[8],
            '备注': row[9]
        }
        test_cases.append(test_case)

    return test_cases

# 运行测试
if __name__ == "__main__":
    pass
