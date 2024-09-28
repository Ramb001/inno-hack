import os
import datetime
import logging
from smtplib import SMTP, SMTP_SSL
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailNotificatior:
    def __init__(self, message: str, receiver: str):
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        logging.info(self.email, self.password)
        self.message = message
        self.receiver = receiver
        self.smtp = SMTP_SSL("smtp.yandex.ru", 465)

    def send_email(self):
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        msg = MIMEMultipart()
        msg.attach(
            MIMEText(
                f"From: {self.email}\nTo: {self.receiver}\nSubject: New task was added\nDate: {date}\n\n{self.message}",
                "plain",
                "utf-8",
            )
        )

        self.smtp.login(self.email, self.password)
        self.smtp.sendmail(self.email, self.receiver, msg)
        self.smtp.quit()
