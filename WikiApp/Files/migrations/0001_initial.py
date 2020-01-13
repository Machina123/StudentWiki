# Generated by Django 2.2.7 on 2020-01-13 19:58

import Files.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('file_id', models.CharField(default=Files.models.generate_id, editable=False, max_length=6, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=250, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('file', models.FileField(max_length=250, upload_to='uploads/', verbose_name='File')),
            ],
        ),
    ]
