from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
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
    success_url = reverse_lazy("files:file_list")

    def get_success_url(self):
        return self.success_url

    def form_valid(self, form):
        f = form.save(commit=False)
        f.file_owner = self.request.user
        f.save()
        return HttpResponseRedirect(self.get_success_url())

@login_required(login_url=reverse_lazy("user:my_login"))
def remove_file(request, pk):
    resource_obj = FileModel.objects.get(pk=pk)
    if resource_obj.file_owner == request.user:
        resource_obj.delete(keep_parents=True)
    return HttpResponseRedirect(reverse_lazy("files:file_list"))