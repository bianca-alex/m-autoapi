# coding=utf-8
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from utils.loader_config import Config
# import ssl
from utils.logger import logger
import mimetypes

class EmailSender:
    def __init__(self, recipient_email, subject, body):
        self.cf = Config()
        self.sender_email = self.cf.get('sender_email', 'Email')
        self.sender_password = self.cf.get('sender_password', 'Email')
        self.recipient_email = recipient_email
        self.subject = subject
        self.body = body

    def attach_file(self, file_path):
        # 创建一个MIMEApplication对象
        with open(file_path, 'rb') as file:
            attachment = MIMEApplication(file.read(), _subtype=self.get_mime_subtype(file_path))  # 根据文件类型修改 _subtype

        # 添加附件的标题
        attachment.add_header('Content-Disposition', 'attachment', filename=file_path)

        # 将附件添加到邮件
        self.msg.attach(attachment)

    def get_mime_subtype(self, file_path):
        mime_type, encoding = mimetypes.guess_type(file_path)
        if mime_type:
            _, subtype = mime_type.split('/')
            return subtype
        else:
            return None

    def send_email(self, attachment_file_path=None):
        # 创建 MIMEMultipart 对象
        msg = MIMEMultipart()

        # 设置发件人、收件人、主题
        msg['From'] = self.cf.get('sender_email', 'Email')
        msg['To'] = self.recipient_email
        msg['Subject'] = self.subject

        # 添加邮件正文
        msg.attach(MIMEText(self.body, 'plain'))

        # 如果提供了附件文件路径，添加附件
        if attachment_file_path:
            self.attach_file(attachment_file_path)
        # 连接到 SMTP 服务器
        # context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
        with smtplib.SMTP(self.cf.get('smtp', 'Email'), self.cf.get('port', 'Email')) as server:
            try:
                server.starttls()
                # 登录发件人邮箱
                server.login(self.sender_email, self.sender_password)
                server.ehlo()
                # 发送邮件
                server.sendmail(self.sender_email, self.recipient_email, msg.as_string())
                logger.info("邮件发送成功")
            except Exception as e:
                logger.error(f"邮件发送失败: {e}")

if __name__ == "__main__":
    pass