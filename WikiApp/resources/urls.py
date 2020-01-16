from django.conf.urls import url
from django.urls import path
from .views import ResourceAddView, ResourceDetailView, ResourceListView, remove_resource

app_name = 'resources'

urlpatterns = [
    url(r'list/', ResourceListView.as_view(), name="resource_list"),
    url(r'add/', ResourceAddView.as_view(), name="resource_add"),
    path("<str:pk>/", ResourceDetailView.as_view(), name="resource_detail"),
    path("<str:pk>/delete/", remove_resource, name="resource_remove")
]