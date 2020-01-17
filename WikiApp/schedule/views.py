from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

import bs4 as bs
import urllib.request
import json
import re
from selenium import webdriver
from time import sleep

from .Handler import *
from schedule.forms import ScheduleSelection

def load_file(path):
    with open(path, 'r', encoding='utf8') as jf:
        data = json.load(jf)
        return data

def load_empty_json_file():
    json_data = [
        {"nazwaPrzedmiotu": "",
         "prowadzacy": "",
         "data": "",
         "dzien": "",
         "poczatek": "",
         "koniec": "",
         "sala": "",
         "forma": "",
         "semestr":"",
         "formaStudiow":"",
         "stopien": "",
         "grupa": ""}]
    with open('schedule/jsonFiles/empty_table.json', 'w', encoding='utf8') as outfile:
        json.dump(json_data, outfile, ensure_ascii=False)

def json_request(request):
    data = load_file('schedule/jsonFiles/empty_table.json')
    return HttpResponse(json.dumps(data))


def schedule_form(request):
    data = load_file('schedule/jsonFiles/json_raw_data.json')
    form = ScheduleSelection()
    load_empty_json_file()
    list = []
    if request.method == "POST":
        form = ScheduleSelection(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            for x in data:
                if cd['date'] == "blank":
                    if x['formaStudiow'] == cd['collageForm'] and x['stopien'] == cd['degree'] and x['semestr'] == cd['year'] and (x['grupa'] == 'W' or re.search('L[0-9]', x['grupa']) or "A" in x['grupa'] or cd['speciality'] in x['grupa']):
                        list.append(x)
                else:
                    if x['formaStudiow'] == cd['collageForm'] and x['stopien'] == cd['degree'] and x['semestr'] == cd['year'] and x['data'] == cd['date'] and (x['grupa'] == 'W' or re.search('L[0-9]', x['grupa']) or "A" in x['grupa'] or cd['speciality'] in x['grupa']):
                        list.append(x)
            with open('schedule/jsonFiles/empty_table.json', 'w', encoding='utf8') as outfile:
                json.dump(list, outfile, ensure_ascii=False)
    return render(request, "schedule/schedule.html", {"form": form})

