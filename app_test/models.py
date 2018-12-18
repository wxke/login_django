from django.db import models

# Create your models here.

class User(models.Model):
    UserName = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    user_type = models.IntegerField(default=2)

class Book(models.Model):
    BookName = models.CharField(max_length=32)
    auth = models.CharField(max_length=32)
    date = models.DateField(auto_now_add=True)