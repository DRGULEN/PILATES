import os
import time
import logging
import requests
from bs4 import BeautifulSoup
from telegram import Bot

# Logging ayarları
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Çevresel değişkenlerden Telegram bilgilerini al
TELEGRAM_TOKEN = os.getenv("8132663035:AAHsvg_CzX8d7kWHjt6uYzVKYt94Nni6iMc")
CHAT_ID = os.getenv("946111573")

if not TELEGRAM_TOKEN or not CHAT_ID:
    logger.error("TELEGRAM_TOKEN ve CHAT_ID çevresel değişkenleri tanımlanmalı!")
    exit(1)

bot = Bot(token=8132663035:AAHsvg_CzX8d7kWHjt6uYzVKYt94Nni6iMc)

URL = "https://www.tcf.gov.tr/branslar/pilates/#kurs"
Pilates | Branşlar | Türkiye Cimnastik Federasyonu - TCF
Tanıtım. Pilates, Joseph Pilates’ in “kontroloji” adını verdiği metodu, zihin ve beden bütünlüğü öngören, denge nefes ve hareket sistemlerinin bir sentezidir.
www.tcf.gov.tr
"
previous_courses = []

def get_courses():
    try:
        response = requests.get(URL)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        kurslar = []
        kurs_container = soup.find("div", id="kurs")
        if not kurs_container:
            logger.warning("Kurs container bulunamadı, sayfa yapısı değişmiş olabilir.")
            return []

        for kurs in kurs_container.find_all("li"):
            kurs_text = kurs.get_text(strip=True)
            if kurs_text:
                kurslar.append(kurs_text)

        return kurslar

    except Exception as e:
        logger.error(f"Kurslar alınırken hata: {e}")
        return []

def check_new_courses():
    global previous_courses
    current_courses = get_courses()
    if not current_courses:
        logger.info("Kurslar alınamadı veya boş döndü.")
        return

    new_courses = [kurs for kurs in current_courses if kurs not in previous_courses]

    if new_courses:
        for kurs in new_courses:
            message = f"Yeni Pilates kursu eklendi:\n{kurs}"
            try:
                bot.send_message(chat_id=CHAT_ID, text=message)
                logger.info(f"Bildirim gönderildi: {kurs}")
            except Exception as e:
                logger.error(f"Telegram mesaj gönderilirken hata: {e}")
        previous_courses = current_courses
    else:
        logger.info("Yeni kurs bulunamadı.")

def main():
    global previous_courses
    previous_courses = get_courses()
    if not previous_courses:
        logger.error("İlk kurslar alınamadı. Bot kapanıyor.")
        return

    logger.info("Bot başladı, kurslar takip ediliyor...")
    while True:
        check_new_courses()
        time.sleep(3600)  # 1 saatte bir kontrol

if __name__ == "__main__":
    main()
