from django.conf.urls import url
from Registration import views
from django.conf import settings
from django.contrib.auth import views as auth_views

app_name = "Registration"
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include('frontend.urls')),
# ]
urlpatterns=[
    url(r'register/', views.register, name='register'),
    url(r'^my_login/$', views.my_login, name='my_login'),
    url(r'^my_logout/$', views.my_logout, name='my_logout'),
    # url(r'logout/', auth_views.LogoutView.as_view(), {'next_page': 'login'}, name='logout'),

    url(r'account_activation_sent/', views.account_activation_sent,
        name='account_activation_sent'),
    url(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        views.activate, name='activate'),
]