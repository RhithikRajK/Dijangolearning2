from django import forms
from .models import MyModel
from ckeditor.widgets import CKEditorWidget

class MyForm(forms.ModelForm):
    body = forms.CharField(widget=CKEditorWidget(),label="Text Editor")
    class Meta:
        model = MyModel
        fields = ('body',)
