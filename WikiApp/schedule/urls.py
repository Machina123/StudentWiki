from django.conf.urls import url
from schedule import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path, include
from django.contrib import admin


app_name = "schedule"

urlpatterns = [
    path('json_request/', views.json_request, name='json_request'),
    url('', views.schedule_form, name='schedule'),
]