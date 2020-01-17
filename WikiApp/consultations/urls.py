from django.conf.urls import url

from .views import show_consultations

app_name = "consultations"

urlpatterns = [
    url("", show_consultations, name="consultations")

]
