import os
import datetime
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib


class EmailNotificatior:
    def __init__(
        self,
        receivers: list[str],
        message,
    ):
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.receivers = receivers
        self.message = message

    def send_email(self, header):
        msg = MIMEText(self.message, "plain", "utf-8")
        msg["Subject"] = Header(header, "utf-8")
        msg["From"] = self.email
        msg["To"] = ", ".join(self.receivers)

        try:
            with smtplib.SMTP_SSL("smtp.yandex.ru", 465, timeout=10) as server:
                server.login(self.email, self.password)
                server.sendmail(self.email, self.receivers, msg.as_string())
                print("Письмо успешно отправлено!")
        except Exception as ex:
            print(f"Ошибка при отправке письма: {ex}")
