FROM python:3.10.4-slim-buster
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE 1

COPY . /app
WORKDIR /app
ENV BOT_TOKEN=""
ENV MESSAGE=""
ENV RECIPIENT=""

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python3","send_message.py"]
