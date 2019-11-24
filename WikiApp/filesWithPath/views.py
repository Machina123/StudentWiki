from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from rest_framework import viewsets
from .models import FileWithPath
from .serializers import FileWithPathSerializer


class FileWithPathViewSet(viewsets.ModelViewSet):
    queryset = FileWithPath.objects.all()
    serializer_class = FileWithPathSerializer


