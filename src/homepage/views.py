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
        blog2=[]
        ucat=temp2.ucategory.split(",")[1:]
        print('here')
        for i in blog:
            print('here2')
            temp=i.category.split(",")[1:]
            print(temp,ucat)
            if set(temp)&set(ucat):
                blog2.append(i.title)
                print('here3')
        params={'cat':catg,'blog':blog,'blog2':blog2,'ucat':ucat}
        return render(request,'index.html',params)
    else:
        return render(request,'login.html')
