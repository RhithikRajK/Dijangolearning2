from django import forms
from .models import Register

class form_cre(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta():
        model = Register
        fields = '__all__'