import os
import datetime

from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailNotification:
    def __init__(self, message: str, receiver: str):
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.message = message
        self.receiver = receiver
        self.smtp = SMTP()

    def send_email(self):
        self.smtp.connect("smtp.yandex.ru", 465)
        self.smtp.login(self.email, self.password)
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        msg = f"From: {self.email}\nTo: {self.receiver}\nSubject: New task was added\nDate: {date}\n\n{self.message}"
        self.smtp.sendmail(self.email, self.receiver, msg)
        self.smtp.quit()
