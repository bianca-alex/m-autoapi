import datetime
import pytest
from utils.assertaction import assert_tool
from utils.http_client import HttpClient
from utils.loader_config import Config
from utils.logger import logger

class TestExample:
    def setup_class(cls):
        logger.info("***** 开始执行测试用例 *****")
        cls.site = Config('site').get('baidu', 'Site')
        cls.client = HttpClient(cls.site)

    def teardown_class(cls):
        logger.info("***** 测试用例执行结束 *****")

    def test_example(self):
        logger.info("test_example")
        res = self.client.get('')
        assert_tool.assert_status_code(res, 200)

if __name__ == "__main__":
    pytest.main(['-o', 'reruns=3'])
