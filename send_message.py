import os

import requests

BOT_TOKEN = os.environ.get("BOT_TOKEN")
MESSAGE = os.environ.get("MESSAGE")
RECIPIENT = os.environ.get("RECIPIENT")
base_url = f"https://api.telegram.org/bot{BOT_TOKEN}"
api_endpoint = f"{base_url}/sendMessage?chat_id={RECIPIENT}&text={MESSAGE}"
requests.post(api_endpoint)
