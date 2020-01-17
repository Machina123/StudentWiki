import bs4 as bs
import urllib.request
from selenium import webdriver
from time import sleep
import json

faculityID = "32"

doJsona = []
elem = []
elemS = {}

url = "https://harmonogram.up.krakow.pl/?faculity=" + faculityID

browser = webdriver.Chrome("C:\chromedriver.exe")
browser.get(url)
sleep(10)
html = browser.page_source
browser.quit()

soup = bs.BeautifulSoup(html, "html.parser")

for x in soup.find_all('tbody'):
    for y in soup.find_all('td'):
        elem.append(y.get_text())

for x in range(0, (int)(len(elem) / 16)):
    elemS = {
        'nazwaPrzedmiotu': elem[0 + x * 16],
        'prowadzacy': elem[1 + x * 16],
        'data': elem[2 + x * 16],
        'dzien': elem[3 + x * 16],
        'poczatek': elem[4 + x * 16],
        'koniec': elem[5 + x * 16],
        'sala': elem[6 + x * 16],
        'forma': elem[7 + x * 16],
        'semestr': elem[8 + (x * 16 + 2)],
        'formaStudiow': elem[9 + (x * 16 + 2)],
        'stopien': elem[10 + (x * 16 + 2)],
        'grupa': elem[11 + (x * 16 + 4)]
    }
    doJsona.append(elemS)

with open('jsonFiles/json_raw_data.json', 'w', encoding='utf8') as outfile:
    json.dump(doJsona, outfile, ensure_ascii=False)