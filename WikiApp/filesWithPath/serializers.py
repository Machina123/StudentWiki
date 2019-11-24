from rest_framework import serializers
from .models import FileWithPath


class FileWithPathSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileWithPath
        fields = '__all__'


