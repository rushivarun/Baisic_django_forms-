from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

# start form

class UserForm(forms.ModelForm):
    model = User
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    model = UserProfileInfo
    class Meta():
        model = UserProfileInfo
        fields = ('portfolio_site', 'profile_pic')
