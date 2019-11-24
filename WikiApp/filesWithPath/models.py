from django.db import models


class FileWithPath(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=80)
    pathToFile = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    login = models.CharField(max_length=15)
    status = models.CharField(max_length=30)

# Create your models here.
