from django.conf.urls import url
from django.urls import path
from .views import FileListView, FileDetailView, FileUploadView

app_name = 'files';

urlpatterns = [
    url(r'list/', FileListView.as_view(), name="file_list"),
    url(r'upload/', FileUploadView.as_view(), name="file_upload"),
    path("<str:pk>/", FileDetailView.as_view(), name="file_detail")
]