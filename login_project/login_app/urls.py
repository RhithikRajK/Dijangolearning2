from django.urls import re_path
from . import views

app_name = 'login_app'

urlpatterns = [
    re_path(r'^register/',views.FormViews,name='register'),
    re_path(r'^login/',views.login,name='login')
]