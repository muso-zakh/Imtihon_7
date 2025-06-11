from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser


class Register(AbstractUser):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    organization = models.CharField(max_length=255)
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=8)
    password2 = models.CharField(max_length=8)
    scientific_degree = models.CharField(max_length=50, null=True)


    def __str__(self):
        return self.first_name
