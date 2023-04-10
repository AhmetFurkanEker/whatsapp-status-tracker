import selenium
from selenium import webdriver
from bs4 import BeautifulSoup
import datetime
import requests

# Telegram bot token ve kullanıcı adı
TOKEN = "..."
USER_ID = "..."

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')

def page_source():
    html = driver.page_source
    soup = BeautifulSoup(html)
    for status in soup.find_all('header'):
        if "çevrimiçi" in status.text:
            now = datetime.datetime.now()
            message = f"{now} : çevrimiçi"
            send_telegram_message(message)
        elif "yazıyor" in status.text:
            now = datetime.datetime.now()
            message = f"{now} : yazıyor"
            send_telegram_message(message)
    return

def send_telegram_message(message):
    # Telegram bot API endpoint
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    # HTTP isteği yapılıyor
    params = {"chat_id": USER_ID, "text": message}
    response = requests.post(url, data=params)

    # Yanıt kontrol ediliyor
    if response.status_code != 200:
        raise ValueError("Mesaj gönderilemedi.")

while True:
    page_source()
