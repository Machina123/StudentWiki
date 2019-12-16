from django.db import models


class File(models.Model):
    auto_generated_ID = models.CharField(max_length=30)
    path = models.CharField(max_length=1000)
    is_local = models.BooleanField()
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
