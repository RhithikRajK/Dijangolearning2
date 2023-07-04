from django.shortcuts import render
from .forms import MyForm
from .models import MyModel

# Create your views here.

def MyView(request):
    form = MyForm()
    return render(request,'html_app/base.html',{'form':form})

