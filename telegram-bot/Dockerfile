FROM python:3.10-slim

WORKDIR /app

COPY ./telegram-bot/requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

COPY ./telegram-bot /app

CMD ["python", "main.py"]