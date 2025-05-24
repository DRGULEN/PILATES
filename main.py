Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> mport requests
  File "<python-input-0>", line 1
    mport requests
          ^^^^^^^^
SyntaxError: invalid syntax
>>> from bs4 mport BeautfulSoup
  File "<python-input-1>", line 1
    from bs4 mport BeautfulSoup
             ^^^^^
SyntaxError: invalid syntax
>>> mport os
  File "<python-input-2>", line 1
    mport os
          ^^
SyntaxError: invalid syntax
>>> mport tme
  File "<python-input-3>", line 1
    mport tme
          ^^^
SyntaxError: invalid syntax
>>>
>>> URL = "https://www.tcf.gov.tr/branslar/plates/kurs"
>>> TELEGRAM_TOKEN = os.envron.get("TELEGRAM_TOKEN")
Traceback (most recent call last):
  File "<python-input-6>", line 1, in <module>
    TELEGRAM_TOKEN = os.envron.get("TELEGRAM_TOKEN")
                     ^^
NameError: name 'os' is not defined. Did you forget to import 'os'?
>>> TELEGRAM_CHAT_ID = os.envron.get("TELEGRAM_CHAT_ID")
Traceback (most recent call last):
  File "<python-input-7>", line 1, in <module>
    TELEGRAM_CHAT_ID = os.envron.get("TELEGRAM_CHAT_ID")
                       ^^
NameError: name 'os' is not defined. Did you forget to import 'os'?
>>> KURS_KAYIT = "kaytl_kurslar.txt"
>>>
>>> def get_courses():
...         response = requests.get(URL)
...             soup = BeautfulSoup(response.text, "html.parser")
...                 kurslar = ]
...
  File "<python-input-10>", line 3
    soup = BeautfulSoup(response.text, "html.parser")
IndentationError: unexpected indent
>>>      Kurs tablosunu bul
  File "<python-input-11>", line 1
    Kurs tablosunu bul
IndentationError: unexpected indent
>>>     kurs_tablosu = soup.fnd("table")
  File "<python-input-12>", line 1
    kurs_tablosu = soup.fnd("table")
IndentationError: unexpected indent
>>>     f kurs_tablosu:
  File "<python-input-13>", line 1
    f kurs_tablosu:
IndentationError: unexpected indent
>>>         satrlar = kurs_tablosu.fnd_all("tr"):   Başlık satırını atla
  File "<python-input-14>", line 1
    satrlar = kurs_tablosu.fnd_all("tr"):   Başlık satırını atla
IndentationError: unexpected indent
>>>         for satr n satrlar:
  File "<python-input-15>", line 1
    for satr n satrlar:
IndentationError: unexpected indent
>>>             hucreler = satr.fnd_all("td")
  File "<python-input-16>", line 1
    hucreler = satr.fnd_all("td")
IndentationError: unexpected indent
>>>             f len(hucreler) = 3:
  File "<python-input-17>", line 1
    f len(hucreler) = 3:
IndentationError: unexpected indent
>>>                 baslk = hucreler.get_text(strp=True)
  File "<python-input-18>", line 1
    baslk = hucreler.get_text(strp=True)
IndentationError: unexpected indent
>>>                 yer = hucreler.get_text(strp=True)
  File "<python-input-19>", line 1
    yer = hucreler.get_text(strp=True)
IndentationError: unexpected indent
>>>                 tarh = hucreler].get_text(strp=True)
  File "<python-input-20>", line 1
    tarh = hucreler].get_text(strp=True)
IndentationError: unexpected indent
>>>                 kurslar.append(f"baslk - yer - tarh")
  File "<python-input-21>", line 1
    kurslar.append(f"baslk - yer - tarh")
IndentationError: unexpected indent
>>>     return kurslar
  File "<python-input-22>", line 1
    return kurslar
IndentationError: unexpected indent
>>>
>>> def load_prevous_courses():
...             try:
...                                 wth open(KURS_KAYIT, "r", encodng="utf-8") as f:
...                                                         return f.read().spltlnes()
...                                                             except FleNotFoundError:
...                                                                                 return ]
...
  File "<python-input-24>", line 6
    return ]
           ^
SyntaxError: unmatched ']'
>>> def save_courses(kurslar):
...                 wth open(KURS_KAYIT, "w", encodng="utf-8") as f:
...                                         for kurs n kurslar:
...                                                                     f.wrte(kurs + "n")
...
  File "<python-input-25>", line 2
    wth open(KURS_KAYIT, "w", encodng="utf-8") as f:
        ^^^^
SyntaxError: invalid syntax
>>> def send_telegram_message(message):
...                     url = f"https://ap.telegram.org/botTELEGRAM_TOKEN/sendMessage"
...                         data =
...                                 "chat_d": TELEGRAM_CHAT_ID,
...                                         "text": message
...
  File "<python-input-26>", line 3
    data =
IndentationError: unexpected indent
>>>     requests.post(url, data=data)
  File "<python-input-27>", line 1
    requests.post(url, data=data)
IndentationError: unexpected indent
>>>
>>> def man():
...                         whle True:
...                                                         mevcut = get_courses()
...                                                                 oncek = load_prevous_courses()
...                                                                         fark =  for k n mevcut f k not n oncek
...
  File "<python-input-29>", line 2
    whle True:
         ^^^^
SyntaxError: invalid syntax
>>>         f fark:
  File "<python-input-30>", line 1
    f fark:
IndentationError: unexpected indent
>>>             mesaj = "\ud83c\udd95 Yen Plates Kursları:n" + "n".jon(fark)
UnicodeEncodeError: 'utf-8' codec can't encode characters in position 21-22: surrogates not allowed
>>>             send_telegram_message(mesaj)
  File "<python-input-32>", line 1
    send_telegram_message(mesaj)
IndentationError: unexpected indent
>>>             save_courses(mevcut)
  File "<python-input-33>", line 1
    save_courses(mevcut)
IndentationError: unexpected indent
>>>
>>>         tme.sleep(3600 * 6)   6 saatte br kontrol
  File "<python-input-35>", line 1
    tme.sleep(3600 * 6)   6 saatte br kontrol
IndentationError: unexpected indent
>>>
>>> f __name__ == "__man__":
  File "<python-input-37>", line 1
    f __name__ == "__man__":
      ^^^^^^^^
SyntaxError: invalid syntax
>>>     man()
