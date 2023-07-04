from django.urls import re_path
from . import views

app_name = 'login_app'

urlpatterns = [
    re_path(r'^$',views.calculator,name='calculator')
]