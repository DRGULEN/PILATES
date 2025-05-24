import requests
from bs4 import BeautifulSoup
import datetime
import time
import os

# Telegram bilgileriniz (Render ortam değişkenlerinden alınıyor)
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

# Daha önce görülen tarihler
known_dates = set()

# Web sayfası URL'si
URL = "https://www.tcf.gov.tr/faaliyetler/"

# Kurs sayfasını çek ve yeni tarihleri bul
def fetch_course_dates():
    response = requests.get(URL)
    soup = BeautifulSoup(response.content, "html.parser")
    
    # Tüm metinlerden tarihleri ayıkla
    raw_text = soup.get_text()
    dates = set()

    for part in raw_text.split():
        try:
            if any(month in part for month in [
                "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", 
                "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"
            ]):
                dates.add(part)
        except Exception:
            continue

    return dates

# Telegram'a mesaj gönder
def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    requests.post(url, data=payload)

# Ana döngü
def monitor():
    global known_dates

    while True:
        try:
            current_dates = fetch_course_dates()
            new_dates = current_dates - known_dates

            for date in new_dates:
                if any(str(yil) in
