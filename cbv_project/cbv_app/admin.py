from django.contrib import admin
from cbv_app.models import Employee, Company

# Register your models here.
admin.site.register(Company)
admin.site.register(Employee)