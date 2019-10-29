from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Category,Blog
# Create your views here.

def index(request):
    catg= Category.objects.all()
    params={'cat':catg}
    return render(request,'addpost.html',params)

def postsubmit(request):
    print('hello')
    mycategory=request.GET.get('categ','no value')
    mytitle=request.GET.get('title','no value')
    mycontent=request.GET.get('content','no value')
    print(mytitle,mycontent,mycategory)
    Blog.objects.create(title=mytitle,category=mycategory,content= mycontent)
    return HttpResponse("submitted")
    