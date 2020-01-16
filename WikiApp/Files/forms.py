from django import forms

from resources.models import Subject
from .models import FileModel

from django.utils.translation import ugettext_lazy as _


class FileUploadForm(forms.ModelForm):
    file_subject = forms.ModelChoiceField(queryset=Subject.objects.all(), empty_label="--------", label=_("Subject"))

    class Meta:
        model = FileModel
        exclude = ["file_id", "file_owner"]
