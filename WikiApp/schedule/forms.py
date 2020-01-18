from django import forms
from.form_choises import *

class ScheduleSelection(forms.Form):
    CHOICES_DATE = CHOICES_DATE
    CHOICES_FORM = CHOICES_FORM
    CHOICES_DEGREE = CHOICES_DEGREE
    CHOICES_YEAR = CHOICES_YEAR
    CHOICES_SPECIALITY = CHOICES_SPECIALITY

    date = forms.ChoiceField(required=True, choices=CHOICES_DATE)
    date.widget.attrs.update({'class' : 'form-control'})
    collageForm = forms.ChoiceField(required=True, choices=CHOICES_FORM)
    collageForm.widget.attrs.update({'class': 'form-control'})
    degree = forms.ChoiceField(required=True, choices=CHOICES_DEGREE)
    degree.widget.attrs.update({'class': 'form-control'})
    year = forms.ChoiceField(required=True, choices=CHOICES_YEAR)
    year.widget.attrs.update({'class': 'form-control'})
    speciality = forms.ChoiceField(required=True, choices=CHOICES_SPECIALITY)
    speciality.widget.attrs.update({'class': 'form-control'})

