from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(unique=True,max_length=200)
    age = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Schools(models.Model):
    name = models.ForeignKey(Student,on_delete=models.CASCADE)
    school_name = models.CharField(max_length=300)

    def __str__(self):
        return self.school_name