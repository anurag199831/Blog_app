from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Category,Blog,UserData
# Create your views here.

def submitcategory(request):
    catg= Category.objects.all()
    print('test')
    selected=''
    for i in catg:
        temp=request.GET.get(i.name,'no value')
        if temp != 'no value':
            selected=selected+','+i.name
    print(selected)
    curremail=request.user.email
    UserData.objects.create(uemail=curremail,ucategory=selected)
    catg= Category.objects.all()
    blog= Blog.objects.all()
    params={'cat':catg,'blog':blog}
    return render(request,'index.html',params)
    


def index(request):
    curremail=request.user.email
    temp=UserData.objects.filter(uemail=curremail).exists()
    
    catg= Category.objects.all()
    blog= Blog.objects.all()
    params={'cat':catg,'blog':blog}
    if temp:
        return render(request,'index.html',params)
    else:
        return render(request,'selectcat.html',params)