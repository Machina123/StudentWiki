from django.conf.urls import url
from rest_framework import routers

from .views import FileWithPathViewSet

router = routers.DefaultRouter()
router.register(r'fileWithPath', FileWithPathViewSet)

urlpatterns = router.urls

