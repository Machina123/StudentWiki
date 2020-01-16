from django.contrib.auth.models import User
from django.db import models
import string
import random
from django.utils.translation import ugettext_lazy as _

from resources.models import Subject


def generate_id():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(6))


class FileModel(models.Model):
    file_id = models.CharField(max_length=6, editable=False, primary_key=True, default=generate_id)
    title = models.CharField(max_length=250, name="title", verbose_name=_("Title"))
    description = models.TextField(name="description", verbose_name=_('Description'))
    file = models.FileField(upload_to="uploads/", max_length=250, name="file", verbose_name=_("File"))
    file_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="file_subject",
                                     verbose_name=_("Subject"))
    file_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="file_owner")

    def delete(self, *args, **kwargs):
        # You have to prepare what you need before delete the model
        storage, path = self.file.storage, self.file.path
        # Delete the model before the file
        super().delete(*args, **kwargs)
        # Delete the file after the model
        storage.delete(path)
