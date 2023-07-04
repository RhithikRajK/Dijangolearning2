from django.urls import re_path
from . import views

app_name = 'first_app'

urlpatterns=[
    re_path(r'^login',views.login,name='login'),
    re_path(r'register',views.FormViews,name='regsiter'),
    re_path(r'^static/',views.index,name='index')
]