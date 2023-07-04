from django import forms
from Exer_App.models import Employee

class FORMSBASICS(forms.ModelForm):
    class Meta():
        model = Employee
        fields = '__all__'
