import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header


# 从 GitHub Actions Secrets 读取 Gmail 配置
GMAIL_USERNAME = os.environ["GMAIL_USERNAME"]
GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]
GMAIL_TO = os.environ["GMAIL_TO"]


def send_email():
    subject = "emiamily 历史上的今天｜测试"

    body = """\
这是 emiamily History 自动化测试邮件。

如果你收到这封邮件，说明：

GitHub Actions
↓
Python
↓
Gmail

已经成功连接。

下一步将接入 X 搜索功能。
"""

    message = MIMEText(body, "plain", "utf-8")
    message["Subject"] = Header(subject, "utf-8")
    message["From"] = GMAIL_USERNAME
    message["To"] = GMAIL_TO

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(
            GMAIL_USERNAME,
            GMAIL_APP_PASSWORD
        )

        server.sendmail(
            GMAIL_USERNAME,
            GMAIL_TO,
            message.as_string()
        )


if __name__ == "__main__":
    send_email()
