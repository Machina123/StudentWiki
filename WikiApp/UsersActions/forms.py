from django import forms
from UsersActions.models import UserProfile
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    username = forms.CharField(max_length=254, help_text='Type your username')
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(max_length=254, help_text='Required. You need email from UP Krakow')

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
