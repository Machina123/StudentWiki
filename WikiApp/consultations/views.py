from django.shortcuts import render
from django.http import HttpResponse
import json


def show_consultations(request):
    with open("consultations/data/wykladowcy.json", "r", encoding="utf8") as plik:
        dane = json.load(plik)
    return render(request, "consultations/main.html",{"data":dane})
