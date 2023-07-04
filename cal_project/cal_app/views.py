from django.shortcuts import render

# Create your views here.
def calculator(request):
    if request.method == 'POST':
        result = 0
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        op = request.POST.get('op')
        if op == 'add':
            result = int(num1) + int(num2)
        elif op == 'sub':
            result = int(num1) - int(num2)
        elif op == 'mul':
            result = int(num1) * int(num2)
        elif op == 'div':
            result = int(num1) / int(num2)
        return render(request,'cal_app/base.html',{'answer':result})
    return render(request,'cal_app/base.html')
