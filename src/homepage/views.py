from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Blog

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        catg= Category.objects.all()
        blog= Blog.objects.all()
        params={'cat':catg,'blog':blog}
        return render(request,'index.html',params)
    else:
        return render(request,'login.html')
