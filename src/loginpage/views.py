from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Category,Blog,UserData
# Create your views here.

def submitcategory(request):
    print('hello2')
    catg= Category.objects.all()
    selected=''
    for i in catg:
        temp=request.GET.get(i.name,'no value')
        if temp != 'no value':
            selected=selected+','+i.name
    curremail=request.user.email
    temp=UserData.objects.filter(uemail=curremail).exists()
    # UserData.objects.update_or_create(uemail=curremail,ucategory=selected)
    if temp:
        temp2 = UserData.objects.get(uemail=request.user.email)
        temp2.ucategory=selected
        temp2.save()
    else :
        UserData.objects.create(uemail=curremail,ucategory=selected)
    catg= Category.objects.all()
    blog= Blog.objects.all()
    temp2 = UserData.objects.get(uemail=request.user.email)
    print(temp2.ucategory)
    ucat=temp2.ucategory.split(",")[1:]
    params={'cat':catg,'blog':blog,'ucat':ucat}
    return render(request,'index.html',params)
    

def editcat(request):
    print('hello')
    catg= Category.objects.all()
    blog= Blog.objects.all()
    params={'cat':catg,'blog':blog}
    return render(request,'selectcat.html',params)

def index(request):
    curremail=request.user.email
    temp=UserData.objects.filter(uemail=curremail).exists()
    
    if temp:

        catg= Category.objects.all()
        blog= Blog.objects.all()
        temp2 = UserData.objects.get(uemail=request.user.email)
        print(temp2.ucategory)
        ucat=temp2.ucategory.split(",")[1:]
        params={'cat':catg,'blog':blog,'ucat':ucat}
        return render(request,'index.html',params)
    else:
        catg= Category.objects.all()
        blog= Blog.objects.all()
        params={'cat':catg,'blog':blog}
        return render(request,'selectcat.html',params)