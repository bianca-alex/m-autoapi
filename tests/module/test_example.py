
import pytest
from utils.assertaction import assert_tool
from utils.http_client import HttpClient
from utils.loader_config import Config
from utils.logger import logger
from utils.send_mail import EmailSender
from common.compress import Compressor
from datetime import datetime

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
    #     # 打包文件
    #     current_time = datetime.now()
    #     timestamp = current_time.strftime('%Y-%m-%d_%H-%M-%S')  # 格式化时间戳
    #     compressor = Compressor('all', 'all_' + timestamp)
    #     compressor.compress()

    #     # 发送邮件
    #     recipient_email = "cccyzloong@163.com"  # 可以是 QQ 邮箱或其他邮箱
    #     # 设置邮件主题和内容
    #     email_subject = "Test Email"
    #     email_body = "This is a test email sent from Python."
    #     # 创建 EmailSender 实例
    #     email_sender = EmailSender(recipient_email, email_subject, email_body)
    #     email_sender.attach_file('all_' + timestamp + '.zip')
    #     # 发送邮件
    #     email_sender.send_email()

if __name__ == "__main__":
    pytest.main(['-o', 'reruns=3'])
