from django.db import models
from django.core.validators import RegexValidator


class Customers(models.Model):
    TC = models.CharField(max_length=11, validators=[
        RegexValidator(regex=r'^[1-9]{1}[0-9]{9}[02468]{1}$', message='Invalid TC', code='nomatch')],
                          null=False, unique=True)
    Name = models.CharField(max_length=50)
    Surname = models.CharField(max_length=50)
    Phone = models.CharField(max_length=11)  # format : 0111 111 11 11
    City = models.CharField(max_length=25)
    Town = models.CharField(max_length=25)

    def __str__(self):
        return self.Name + " " + self.Surname
