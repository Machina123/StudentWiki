from django.db import models
from django import forms

class ScheduleSelection(forms.Form):
    WYBORY = [("I Stopnia", "Ist"), ("I Stopnia", "IIst")]
    form = forms.MultipleChoiceField(required=True, widget=forms.CheckboxSelectMultiple, choices=WYBORY)