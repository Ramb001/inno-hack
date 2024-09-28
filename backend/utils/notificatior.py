import os
import datetime
import logging
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailNotificatior:
    def __init__(self, message: str, receiver: str):
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.message = message
        self.receiver = receiver
        self.smtp = SMTP()

    def send_email(self):
        self.smtp.connect("smtp.yandex.ru", 465)
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        msg = MIMEText(
            f"From: {self.email}\nTo: {self.receiver}\nSubject: New task was added\nDate: {date}\n\n{self.message}",
            "plain",
            "utf-8",
        )

        try:
            self.smtp.login(self.email, self.password)
        except Exception as e:
            logging.error(e)

        try:
            self.smtp.sendmail(self.email, self.receiver, msg)
        except Exception as e:
            logging.error(e)
        self.smtp.quit()
