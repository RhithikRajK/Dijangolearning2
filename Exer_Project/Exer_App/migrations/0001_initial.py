# Generated by Django 4.2.2 on 2023-06-14 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('age', models.IntegerField(default=0)),
                ('address', models.CharField(max_length=400)),
            ],
        ),
    ]
