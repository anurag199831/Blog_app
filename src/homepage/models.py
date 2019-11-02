from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)

class Blog(models.Model):
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    content=models.CharField(max_length=10000)
    author=models.CharField(max_length=50,default="")

# class UserData(models.Model):
#     uid=models.IntegerField()
#     usercat[]=models.
    
