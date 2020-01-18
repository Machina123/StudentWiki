from django import forms
from .models import Subject, ExternalResource
from django.utils.translation import ugettext_lazy as _

class ExternalResourceForm(forms.ModelForm):
    rsrc_subject = forms.ModelChoiceField(queryset=Subject.objects.all(), empty_label="-------", label=_("Subject"))
    rsrc_subject.widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = ExternalResource
        exclude = ["resource_id", "rsrc_owner"]