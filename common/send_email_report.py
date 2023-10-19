from datetime import datetime
from common.compress import Compressor
from utils.loader_config import Config
from utils.send_mail import EmailSender

class SendEmailReport:
    def __init__(self, dirname, email_subject, email_body, attach=None):
        # 打包文件


        # 发送邮件
        recipient_email = Config().get('recipient_email', 'Email')

        # 创建 EmailSender 实例
        email_sender = EmailSender(recipient_email, email_subject, email_body)
        # 发送邮件
        if attach == None:
            email_sender.send_email()
        else:
            current_time = datetime.now()
            timestamp = current_time.strftime('%Y-%m-%d_%H-%M-%S')  # 格式化时间戳
            compressor = Compressor(dirname, dirname + '_' + timestamp)
            compressor.compress()
            email_sender.send_email(dirname + '_' + timestamp + '.zip')
        