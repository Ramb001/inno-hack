import os
import datetime
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib


def send_ya_mail(recipients_emails: list, msg_text: str):
    login = "kotov1548@yandex.ru"
    password = "zntvowvgustfrcgh"  # Берем пароль из переменной окружения

    # Создание MIME-сообщения
    msg = MIMEText(msg_text, "plain", "utf-8")
    msg["Subject"] = Header("Важное!!!", "utf-8")
    msg["From"] = login
    msg["To"] = ", ".join(recipients_emails)

    try:
        with smtplib.SMTP_SSL("smtp.yandex.ru", 465, timeout=10) as server:
            server.login(login, password)
            server.sendmail(login, recipients_emails, msg.as_string())
            print("Письмо успешно отправлено!")
    except Exception as ex:
        print(f"Ошибка при отправке письма: {ex}")


class EmailNotificatior:
    def __init__(self, message: str, receivers: list[str]):
        self.smtp = smtplib.SMTP_SSL("smtp.yandex.ru", 465, timeout=10)
        self.message = MIMEText(message, "plain", "utf-8")
        self.email = os.getenv("EMAIL")
        self.password = os.getenv("PASSWORD")
        self.receivers = receivers

    def send_email(self):
        self.message["Subject"] = Header("Важное!!!", "utf-8")
        self.message["From"] = self.email
        self.message["To"] = ", ".join(self.receivers)

        try:
            with self.smtp as server:
                server.login(self.email, self.password)
                server.sendmail(self.email, self.receivers, self.message)
                logging.info(f"Письмо успешно отправлено {self.receivers}")
                server.quit()
        except Exception as ex:
            logging.error(f"Ошибка при отправке письма: {ex}")
