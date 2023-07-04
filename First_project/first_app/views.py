from django.shortcuts import render
from . import forms
from first_app.models import Register

# Create your views here.

def index(request):
    return render(request,'first_app/register.html')

def FormViews(request):
    form = forms.form_cre()
    if request.method == 'POST':
        form = forms.form_cre(data=request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'first_app/register.html',{'forme':'Registered!!! Press login button'})
    return render(request,'first_app/register.html',{'form':form})


def login(request):
    if request.method == 'POST':
        user = request.POST.get('usern')
        passw = request.POST.get('passwo')
        details = Register.objects.filter(username=user,password=passw)
        if details:
            return render(request,'first_app/success.html')
        else:
            return render(request,'first_app/login.html',{'logine':'Not Registered !!!! Press Register button'})
    return render(request,'first_app/login.html')