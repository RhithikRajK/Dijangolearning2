from django.db import models

# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=250)
    location = models.CharField(max_length=400)
    address = models.CharField(max_length=400)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=256)
    age = models.PositiveIntegerField(default=0)
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='employee')

    def __str__(self):
        return self.name