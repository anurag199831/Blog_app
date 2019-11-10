from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Category,Blog,UserData


def index(request):
    if request.user.is_authenticated:
        curremail=request.user.email
    else:
        return render(request,'login.html')
    temp=UserData.objects.filter(uemail=curremail).exists()
    
    catg= Category.objects.all()
    temp2 = UserData.objects.get(uemail=request.user.email)
    ucat=temp2.ucategory.split(",")[1:]
    params={'cat':catg,'ucat':ucat}
    print(ucat)
    if temp:
        return render(request,'addpost.html',params)
    else:
        return HttpResponse("<h1> This is choice selection page <h1>")

def postsubmit(request):
    # mycategory=request.GET.get('categ','no value')
    catg= Category.objects.all()
    selected=''
    for i in catg:
        temp=request.GET.get(i.name,'no value')
        if temp != 'no value':
            selected=selected+','+i.name
    mycategory=selected
    mytitle=request.GET.get('title','no value')
    mycontent=request.GET.get('content','no value')
    myauthor=request.GET.get('author','no value')
    myid=mytitle+myauthor
    Blog.objects.create(bid=myid,title=mytitle,category=mycategory,content= mycontent,author=myauthor)
    return render(request,'postsubmitted.html')
    