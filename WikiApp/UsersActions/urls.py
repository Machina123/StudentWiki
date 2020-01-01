from django.conf.urls import url
from UsersActions import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.urls import path, include
from django.contrib import admin


app_name = "UsersActions"
urlpatterns = [
    url(r'register/', views.register, name='register'),
    url(r'index/', views.index, name='index'),
    url(r'^my_login/$', views.my_login, name='my_login'),
    url(r'^my_logout/$', views.my_logout, name='my_logout'),

    url(r'account_activation_sent/', views.account_activation_sent,
        name='account_activation_sent'),
    url(r'activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
        views.activate, name='activate'),

    url('change-password/', auth_views.PasswordChangeView.as_view(
            template_name='frontend/change-password.html',
            success_url='/'
        ),
        name='change_password'),


    url(r'password-reset/',
        auth_views.PasswordResetView.as_view(
            template_name='frontend/password-reset/password_reset_form.html',
            subject_template_name='frontend/password-reset/password_reset_subject.txt',
            email_template_name='frontend/password-reset/password_reset_email.html',
            success_url='/UsersActions/password_reset/done/',
             ), name='password_reset'),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(
            template_name='frontend/password-reset/password_reset_done.html'
             ), name='password_reset/done/'),
    url(r'password-reset-confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', auth_views.PasswordResetConfirmView.as_view(
            template_name='frontend/password-reset/password_reset_confirm.html',
            success_url='/UsersActions/password-reset-complete/'
             ), name='password_reset_confirm'),
    url(r'password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(
            template_name='frontend/password-reset/password_reset_complete.html'
             ), name='password_reset_complete'),
]