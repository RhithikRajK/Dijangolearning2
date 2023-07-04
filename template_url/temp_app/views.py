from django.shortcuts import render

# Create your views here.
dict = {
    'greet':'Hello World',
    'num':100
}

def index(request):
    return render(request,'temp_app/index.html')

def other(request):
    return render(request,'temp_app/other.html',context=dict)

def rel_url(request):
    return render(request,'temp_app/relative_url.html',context=dict)