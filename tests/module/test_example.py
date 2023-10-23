
import pytest
import os
from utils.assertaction import assert_tool
from utils.http_client import HttpClient
from utils.loader_config import Config
from utils.loader_excel import load_test_case
from utils.logger import logger
from common.send_email_report import SendEmailReport
from common.settings import get_data_path
from .conftest import module_login

case_list = load_test_case(os.path.join(get_data_path(), 'test_cases.xlsx'))

class TestExample:
    def setup_class(self):
        logger.info("***** 开始执行测试用例 *****")
        self.site = Config('site').get('baidu', 'Site')
        self.client = HttpClient(self.site)
        # module_login()

    def teardown_class(self):
        # self.sendMail()
        logger.info("***** 测试用例执行结束 *****")

    def test_example(self):
        logger.info("test_example")
        res = self.client.get('')
        assert_tool.assert_status_code(res, 200)

    # @pytest.mark.skip(reason="Test")
    def sendMail():
        SendEmailReport('all', 'test', 'test', True) # True代表发送附件
    
    # 逻辑书写
    def execute_test_case(self, test_case):
        # 执行测试用例的代码逻辑
        # 可以使用test_case字典中的数据进行请求发送和预期结果验证
        rsp = test_case['预期结果']
        # 请求头替换 实际请求中 Bearer为动态生成
        token = module_login()
        test_case['请求头'] = '{"Content-Type": "application/json", "Authorization": "Bearer ' + token + '"}'
        
        res = self.client.excelTemple(test_case)
        assert_tool.assert_status_code(res, 404)


    @pytest.mark.parametrize('test_case', case_list, ids=lambda test_case: test_case['用例编号'])
    def test_execute_test_case(self, test_case):
        self.execute_test_case(test_case)


if __name__ == "__main__":
    pytest.main(['-o', 'reruns=3'])
