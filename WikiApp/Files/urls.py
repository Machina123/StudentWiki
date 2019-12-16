from django.conf.urls import url
from Files import views

app_name = "Files"

urlpatterns = [
    url(r'files/', views.files, name='files'),
]
