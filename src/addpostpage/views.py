from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Category,Blog,UserData
# Create your views here.


def index(request):
    if request.user.is_authenticated:
        curremail=request.user.email
    else:
        return render(request,'login.html')
    temp=UserData.objects.filter(uemail=curremail).exists()
    
    catg= Category.objects.all()
    params={'cat':catg}
    if temp:
        return render(request,'addpost.html',params)
    else:
        return HttpResponse("<h1> This is choice selection page <h1>")

def postsubmit(request):
    mycategory=request.GET.get('categ','no value')
    mytitle=request.GET.get('title','no value')
    mycontent=request.GET.get('content','no value')
    myauthor=request.GET.get('author','no value')
    Blog.objects.create(title=mytitle,category=mycategory,content= mycontent,author=myauthor)
    return render(request,'postsubmitted.html')
    