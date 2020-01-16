from django.shortcuts import render
import bs4 as bs
import urllib.request
from selenium import webdriver
from time import sleep
import json
import os

from schedule.forms import ScheduleSelection


def load_schedule():
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

    with open('jsonData.json', 'w', encoding='utf8') as outfile:
        json.dump(doJsona, outfile, ensure_ascii=False)

def load_file():
    with open('jsonData.json', 'r', encoding='utf8') as jf:
        data = json.load(jf)
        return data

def get_form():
    data = load_file()
    a = set()
    for x in data:
        a.add(x['formaStudiow'])
    return sorted(a)

def get_degree():
    data = load_file()
    a = set()
    for x in data:
        a.add(x['stopien'])
    return sorted(a)

def get_year(stopien):
    data = load_file()
    a = set()
    for x in data:
        if x['stopien'] == stopien:
            a.add(x['semestr'])
    return sorted(a)

def get_specialty(speciality):
    data = load_file()
    a = set()
    for x in data:
        if speciality in  x['grupa']:
            a.add(x['grupa'])
    return sorted(a)

def get_group(semestr):
    data = load_file()
    a = set()
    for x in data:
        if x['semestr'] == semestr:
            a.add(x['grupa'])
    return sorted(a)

def data_insertion():
    forma = "S"
    stopien = "Ist"
    specjalnosc = "L_ASI1"
    rok = '5 Z'
    grupa = 'L1'

    """with open('jsonData.json', 'r', encoding='utf8') as jf:
        data = json.load(jf)
        a = set()
        for x in data:
            if x['formaStudiow'] == 'S' and x['stopien'] == 'Ist' and x['semestr'] == '5 Z':
                print(x['nazwaPrzedmiotu'])
                print(x['prowadzacy'])
                print(x['data'])
                print(x['dzien'])
                print(x['poczatek'])
                print(x['koniec'])
                print(x['sala'])
                print(x['forma'])
                print(x['semestr'])
                print(x['formaStudiow'])
                print(x['stopien'])
                a.add(x['grupa'])
        print(a)"""
    print("XD")

def schedule_form(request):
    xd = get_form()
    final_string = '<select class="select-1">'
    for x in xd:
        if x != '':
            final_string += '<option value="'+ x +'">'+x+'</option>'
    final_string += '</select>'
    print(final_string)
    dupa = {"aaa": final_string}

    return render(request, "schedule/schedule_main.html", dupa)
    """data = load_file()
    if request.method == "POST":
        form = ScheduleSelection(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            a = cd.get('Ist')
            for x in data:
                if x["form"] == form:
                 print(x['form'])"""
    #print(request.POST.get("form"))
    #return render(request, "schedule/schedule_main.html")
"""

a = get_form()
for x in a:
    print(x, type(x))"""
"""
e = get_degree()
b = get_year(e[1])
c = get_specialty("ASI")
d = get_group(b[1])
print(a)
print(e)
print(b)
print(c)
print(d)"""

