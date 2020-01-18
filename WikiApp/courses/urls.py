from django.conf.urls import url
from django.urls import path
from .views import course_details, courses_list

app_name = 'courses'

urlpatterns = [
    path("<int:pk>/", course_details, name="course_detail"),
    url('', courses_list, name="courses_list")
]