import requests
import os

TOKEN = os.environ["TOKEN"]
url = "https://phoneshop.pythonanywhere.com/home"

payload = {
    "url" : url
}

r = requests.get(f"https://api.telegram.org/bot{TOKEN}/setWebhook", params = payload)

print(r.json())