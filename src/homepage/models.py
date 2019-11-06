from django.db import models
from django.utils import timezone

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title=models.CharField(max_length=100)
    #category=models.ForeignKey(Category,on_delete=models.CASCADE)
    category=models.CharField(max_length=50)
    content=models.CharField(max_length=10000)
    author=models.CharField(max_length=50,default="")
    creation_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering =  ['-creation_date']

class UserData(models.Model):
    uemail=models.CharField(max_length=100,default="")
    ucategory=models.CharField(max_length=1000)
    
