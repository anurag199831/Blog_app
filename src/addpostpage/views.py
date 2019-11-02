from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Category,Blog
# Create your views here.


def index(request):
    catg= Category.objects.all()
    params={'cat':catg}
    return render(request,'addpost.html',params)

def postsubmit(request):
    mycategory=request.GET.get('categ','no value')
    mytitle=request.GET.get('title','no value')
    mycontent=request.GET.get('content','no value')
    myauthor=request.GET.get('author','no value')
    Blog.objects.create(title=mytitle,category=mycategory,content= mycontent,author=myauthor)
    return HttpResponse("submitted")
    