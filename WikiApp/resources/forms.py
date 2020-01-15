from django import forms
from .models import Subject, ExternalResource

class ExternalResourceForm(forms.ModelForm):
    subject = forms.ModelChoiceField(queryset=Subject.objects.all(), empty_label="-------", to_field_name="sub_name")

    class Meta:
        model = ExternalResource
        exclude = ["resource_id"]