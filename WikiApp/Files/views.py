from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import FileModel
from .forms import FileUploadForm

class FileListView(LoginRequiredMixin, ListView):
    model = FileModel
    template_name = "files/file_list.html"
    raise_exception = False
    login_url = "/user/my_login/"

class FileDetailView(LoginRequiredMixin, DetailView):
    template_name = "files/file_detail.html"
    model = FileModel
    login_url = "/user/my_login/"

class FileUploadView(LoginRequiredMixin, CreateView):
    model = FileModel
    template_name = "files/file_upload.html"
    form_class = FileUploadForm
    success_url = reverse_lazy("file_list")