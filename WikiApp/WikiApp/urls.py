"""WikiApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import path, include
from WikiApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('django.contrib.auth.urls')),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]


urlpatterns += i18n_patterns(
    path('', views.homepage, name="homepage"),
    path('user/', include('UsersActions.urls')),
    path('files/', include('Files.urls')),
    path('schedule/', include('schedule.urls')),
    path('resources/', include('resources.urls', namespace="resources")),
    path('consultations/', include('consultations.urls')),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
    path('courses/', include('courses.urls', namespace="courses"))
)
