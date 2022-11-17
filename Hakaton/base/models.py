from django.contrib.auth.models import AbstractUser
from django.db import models


class UserAbstract(AbstractUser):
    # last_name = models.CharField(max_length=40)
    surname = models.CharField(max_length=40)
    # city = models.CharField(max_length=1, choices=)
    data_of_birth = models.DateField(default='2004-01-12')
    # phone_number = models.IntegerField(default=7)


class Category_groups(models.Model):
    group_name = models.CharField(max_length=100)
    groups = models.ManyToManyField(UserAbstract)
