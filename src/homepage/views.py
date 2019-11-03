from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Blog,UserData

# Create your views here.

def index(request):
    if request.user.is_authenticated:
        catg = Category.objects.all()
        blog = Blog.objects.all()
        temp2 = UserData.objects.get(uemail=request.user.email)
        print(temp2.ucategory)
        ucat=temp2.ucategory.split(",")[1:]
        params={'cat':catg,'blog':blog,'ucat':ucat}
        return render(request,'index.html',params)
    else:
        return render(request,'login.html')
