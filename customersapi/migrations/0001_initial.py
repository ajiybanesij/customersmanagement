# Generated by Django 3.2.5 on 2021-07-11 11:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TC', models.CharField(max_length=11, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 11', regex='^[1-9]{1}[0-9]{9}[02468]{1}$')])),
                ('Name', models.CharField(max_length=50)),
                ('Surname', models.CharField(max_length=50)),
                ('Phone', models.CharField(max_length=11)),
                ('City', models.CharField(max_length=25)),
                ('Town', models.CharField(max_length=25)),
            ],
        ),
    ]
