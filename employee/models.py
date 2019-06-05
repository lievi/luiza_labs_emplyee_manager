from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)
    department = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return self.name
