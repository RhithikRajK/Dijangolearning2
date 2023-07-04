from django import forms
from django.forms import CharField
from django.core import validators
from form_app.models import Student, Schools

class FORMSBASICS(forms.ModelForm):
    class Meta():
        model = Student
        fields = '__all__'



