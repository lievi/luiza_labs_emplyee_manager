from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    departament = models.CharField(max_length=30)
