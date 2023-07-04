from django.shortcuts import render
from . import forms
from Exer_App.models import Employee
# Create your views here.

def index(request):
    return render(request,'Exer_App/index.html')

def FormViews(request):
    form = forms.FORMSBASICS()

    if request.method == "POST":
        form = forms.FORMSBASICS(request.POST)
        if form.is_valid():
            form.save(commit=True)

    return render(request, 'Exer_App/form.html',{'form':form})

def form_view(request):
    details = Employee.objects.order_by('age')
    dict = {'employee':details}
    return render(request,'Exer_App/form_view.html',context=dict)