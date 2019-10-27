from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Blog
# Create your views here.

def index(request):
    return render(request,'addpost.html')

def postsubmit(request):
    print('hello')
    mytitle=request.GET.get('title','no value')
    mycontent=request.GET.get('content','no value')
    print(mytitle,mycontent)
    temp=Blog(mytitle,1,mycontent)
    return HttpResponse("submitted")