from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

from .models import ExternalResource
from .forms import ExternalResourceForm
# Create your views here.
from UsersActions.models import UserProfile


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

    def get_success_url(self):
        return self.success_url

    def form_valid(self, form):
        f = form.save(commit=False)
        f.rsrc_owner = self.request.user
        f.save()
        return HttpResponseRedirect(self.get_success_url())

@login_required(login_url=reverse_lazy("user:my_login"))
def remove_resource(request, pk):
    resource_obj = ExternalResource.objects.get(pk=pk)
    if resource_obj.rsrc_owner == request.user:
        resource_obj.delete(keep_parents=True)
    return HttpResponseRedirect(reverse_lazy("resources:resource_list"))