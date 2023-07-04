from django import forms
from user_app.models import UserProfileInfo
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password = forms.CharField(widget = forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfile(forms.ModelForm):
    class Meta():
        model = UserProfileInfo
        fields = '__all__'