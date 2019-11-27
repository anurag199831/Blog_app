from django.db import models
from django.utils import timezone


class Category(models.Model):
    """
    This is the category class

    Args:
        models.Model
 
    """
    name=models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Blog(models.Model):
    """
    This is the class which contains information about fields of a particular Blog

    Args:
        models.Model
 
    """
    bid=models.CharField(max_length=200,default="")
    title=models.CharField(max_length=100)
    category=models.CharField(max_length=50)
    content=models.CharField(max_length=10000)
    author=models.CharField(max_length=50,default="")
    img=models.ImageField(upload_to="post_images",default="",blank=True,null=True)
    vid=models.FileField(upload_to="post_videos",default="",blank=True,null=True)
    imgflag=models.BooleanField(default=False)
    vidflag=models.BooleanField(default=False)
    creation_date=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering =  ['-creation_date']

class UserData(models.Model):
    """
    This is the class which contains information about users who have login

    Args:
        models.Model
 
    """
    uemail=models.CharField(max_length=100,default="")
    ucategory=models.CharField(max_length=1000)
    
