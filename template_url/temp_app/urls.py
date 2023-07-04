from django.urls import re_path
from . import views
app_name = 'temp_app'

urlpatterns = [
    re_path(r'^others/',views.other,name='other'),
    re_path(r'^rel_url/',views.rel_url,name='rel_url')
]