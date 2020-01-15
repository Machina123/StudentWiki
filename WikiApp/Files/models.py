from django.db import models
import string
import random


def generate_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(6))


class FileModel(models.Model):
    file_id = models.CharField(max_length=6, editable=False, primary_key=True, default=generate_id)
    title = models.CharField(max_length=250, name="title", verbose_name="Tytuł")
    description = models.TextField(name="description", verbose_name="Opis")
    file = models.FileField(upload_to="uploads/", max_length=250, name="file", verbose_name="Plik")
