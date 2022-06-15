import email
from django.db import models

# Create your models here.
class Student(models.Model):
    sid = models.IntegerField()
    name = models.CharField(max_length=50)
    addr = models.CharField(max_length=200)
    email = models.EmailField(max_length=200) 