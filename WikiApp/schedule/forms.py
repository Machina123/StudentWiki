from django.db import models
from django import forms

class ScheduleSelection(forms.Form):
    CHOICES = (('Option 1', 'Option 1'), ('Option 2', 'Option 2'),)
    field = forms.ChoiceField(choices=CHOICES)
