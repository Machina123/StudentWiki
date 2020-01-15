from django.db import models
import string
import random
from django.utils.translation import ugettext_lazy as _
# Create your models here.

def generate_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(6))

class Subject(models.Model):
    sub_name = models.CharField(max_length=255, verbose_name=_("Subject"), name="sub_name")

class ExternalResource(models.Model):
    resource_id = models.CharField(max_length=6, editable=False, primary_key=True, default=generate_id)
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    description = models.TextField(verbose_name=_("Description"))
    resource_uri = models.URLField(verbose_name=_("Resource address"))
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="subject")
