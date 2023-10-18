# coding=utf-8
import openpyxl
import os
import pytest
from common.settings import get_data_path

# 从Excel文件中读取测试用例数据
def load_test_data(file_path):
    data_path = get_data_path()
    workbook = openpyxl.load_workbook(os.path.join(data_path, file_path))
    sheet = workbook.active
    test_data = []
    for row in sheet.iter_rows(min_row=2, values_only=True):
        test_data.append(row)
    return test_data

# 运行测试
if __name__ == "__main__":
    pass
