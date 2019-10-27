from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=1000)

class Blog(models.Model):
    title=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    content=models.CharField(max_length=10000)
