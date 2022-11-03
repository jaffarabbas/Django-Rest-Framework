from django.db import models

# Create your models here.
class Employee(models.Model):
    code = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=400)
    phone = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)