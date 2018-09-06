"""
自动发送邮件:
   Python对STMP的支持有两个模块:
        smtplib:负责发送邮件
        email  :负责构造文件

注意:注册邮箱后,需要在设置客户端授权码,第三方登录时是需要输入第三方授权码的
即下面的passwd存储的是第三方授权码

"""
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr, parseaddr


class SendEmail(object):
    """只能实现对一个用户发送邮件"""

    __slots__ = ("from_addr", "to_addr", "passwd", "_msg",
                 "smtp_addr", "smtp_port", "text", "theme")

    def _create_email(self):
        """构造一个纯文本文件:
        MIMEText
            _text --> 发送的正文
            _subtype -->plain表示是文本文件
            _charset -->编码格式
        """
        self._msg = MIMEText(self.text, 'plain', 'utf-8')
        # 设置发件人
        user_name = self.from_addr.split('@')
        self._msg["From"] = self._format_addr('%s <%s>' % (user_name[0], self.from_addr))
        # 设置收件人
        user_name = self.to_addr.split('@')
        self._msg['To'] = self._format_addr('%s <%s>' % (user_name[0], self.to_addr))
        # 设置主题
        self._msg['Subject'] = Header(self.theme, 'utf-8').encode()

    def _format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    def do(self):
        """发送邮件"""
        self._create_email()
        server = smtplib.SMTP(self.smtp_addr, self.smtp_port)  # 获取SMTP server对象
        server.set_debuglevel(1)  # 设置交互信息打印级别
        server.login(self.from_addr, self.passwd)  # 登录smtp server
        server.sendmail(self.from_addr, [self.to_addr], self._msg.as_string())  # 发送邮件
        server.quit()  # 退出server


def send_email_eg():
    email_ = SendEmail()
    # 发送方的邮箱
    email_.from_addr = "xxx@yeah.net"
    # 收件邮箱
    email_.to_addr = "xxx@foxmail.com"
    # 发件方的第三方授权密码
    email_.passwd = "xxx"
    # smtp server
    email_.smtp_addr = "smtp.yeah.net"
    # smtp server port
    email_.smtp_port = 25
    # 发送的内容
    email_.text = 'life is short,I use python.'
    # 主题
    email_.theme = "Python"
    # 发送
    email_.do()


send_email_eg()
