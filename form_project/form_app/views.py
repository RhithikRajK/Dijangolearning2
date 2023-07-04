from django.shortcuts import render
from . import forms
# Create your views here.

def index(request):
    return render(request,'form_app/index.html')

def FormViews(request):
    form = forms.FORMSBASICS()

    if request.method == "POST":
        form = forms.FORMSBASICS(request.POST)

        if form.is_valid():
            form.save(commit=True)

    return render(request,'form_app/form.html',{'form':form})