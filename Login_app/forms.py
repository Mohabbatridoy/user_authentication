from django import forms
from Login_app import models
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.PasswordInput()
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = models.UserInfo
        fields = ('facebook_id', 'profile_pic')