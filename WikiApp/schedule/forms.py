from django import forms
from.form_choises import *

class ScheduleSelection(forms.Form):
    CHOICES_DATE = CHOICES_DATE
    CHOICES_FORM = CHOICES_FORM
    CHOICES_DEGREE = CHOICES_DEGREE
    CHOICES_YEAR = CHOICES_YEAR
    CHOICES_SPECIALITY = CHOICES_SPECIALITY

    date = forms.ChoiceField(required=True, choices=CHOICES_DATE)
    collageForm = forms.ChoiceField(required=True, choices=CHOICES_FORM)
    degree = forms.ChoiceField(required=True, choices=CHOICES_DEGREE)
    year = forms.ChoiceField(required=True, choices=CHOICES_YEAR)
    speciality = forms.ChoiceField(required=True, choices=CHOICES_SPECIALITY)

