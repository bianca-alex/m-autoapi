import datetime
import pytest
from utils.assertaction import assert_tool
from utils.http_client import HttpClient
from utils.loader_config import Config
from utils.logger import logger
from utils.send_mail import EmailSender

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

    # def test_sendMail(self):
    #     recipient_email = "xxx@163.com"  # 可以是 QQ 邮箱或其他邮箱
    #     # 设置邮件主题和内容
    #     email_subject = "Test Email"
    #     email_body = "This is a test email sent from Python."
    #     # 创建 EmailSender 实例
    #     email_sender = EmailSender(recipient_email, email_subject, email_body)
    #     # 发送邮件
    #     email_sender.send_email()

if __name__ == "__main__":
    pytest.main(['-o', 'reruns=3'])
