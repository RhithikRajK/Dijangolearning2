from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^form/',views.FormViews,name='forms'),
    re_path(r'^formv/',views.form_view,name='forms')
]