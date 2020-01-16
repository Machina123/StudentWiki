from django.conf.urls import url
from django.urls import path
from .views import FileListView, FileDetailView, FileUploadView, remove_file
from django.conf import settings
from django.conf.urls.static import static

app_name = 'files'

urlpatterns = [
    url(r'list/', FileListView.as_view(), name="file_list"),
    url(r'upload/', FileUploadView.as_view(), name="file_upload"),
    path("<str:pk>/", FileDetailView.as_view(), name="file_detail"),
    path("<str:pk>/delete/", remove_file, name="file_remove")
]