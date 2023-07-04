from django.shortcuts import render
from user_app.forms import UserForm, UserProfile
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import auth

def index(request):
    return render(request,'user_app/index.html')

@ login_required()
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username='username', password='password')

        if user:
            if user.is_active():
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("You have not registered")
        else:
            print("Someone with then username and password is trying to enter in the system".format(username,password))
            return HttpResponse("User not authenticated")
    else:
        return render(request,'user_app/login.html',{})




def register(request):
    registered = False

    if request.method =='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfile(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.error, profile_form.error)
    else:
        user_form = UserForm()
        profile_form = UserProfile()

    return render(request,'user_app/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})