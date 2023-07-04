import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','First_project.settings')

import django
django.setup()

import random

from first_app.models import *

from faker import Faker

from model_bakery.recipe import Recipe,foreign_key

ages=[3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]
school = ['MontFort','KUP','Delhi Public School','Rani Jai','Narayana']
fake = Faker()

def add_age():
    t = random.choice(ages)
    return t

def add_school():
    t = random.choice(school)
    return t

def populate():
    N=5
    roll = 0
    for i in range(N):
        fakename = fake.name()
        fake_roll_no = roll+1
        roll=roll+1
        fake_id = roll+1
        fake_age = add_age()
        fakeschool = add_school()
        student= Recipe(Student,name=fakename,roll_no=fake_roll_no,age=fake_age)
        school = Recipe(Schools,name=foreign_key(student),school_n=fakeschool)


if __name__=='__main__':
    print("Populating database")
    populate()
    print("Populated!")