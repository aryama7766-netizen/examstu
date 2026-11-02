from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class student(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone=models.BigIntegerField()
    fee=models.IntegerField()
    joining_date=models.DateTimeField(auto_now_add=True)

 