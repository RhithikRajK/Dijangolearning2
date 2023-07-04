from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(unique=True,max_length=200)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=400)

    def __str__(self):
        return self.name
