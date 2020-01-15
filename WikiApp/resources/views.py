from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import ExternalResource
from .forms import ExternalResourceForm
# Create your views here.

class ResourceListView(LoginRequiredMixin, ListView):
    model = ExternalResource
    template_name = "resources/resource_list.html"
    raise_exception = False
    login_url = "/user/my_login/"

class ResourceDetailView(LoginRequiredMixin, DetailView):
    model = ExternalResource
    template_name = "resources/resource_detail.html"
    login_url = "/user/my_login/"

class ResourceAddView(LoginRequiredMixin, CreateView):
    model = ExternalResource
    template_name = "resources/resource_add.html"
    form_class = ExternalResourceForm
    success_url = reverse_lazy("resources:resource_list")