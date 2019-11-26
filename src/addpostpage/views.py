from django.shortcuts import render
from django.http import HttpResponse
from homepage.models import Category,Blog,UserData
import re

def remove_bad_words(inputs):
    badwords = []
    with open('cussWords.txt',"r") as fp:
        for line in fp:
            word = line.strip()
            if word!="":
                badwords.append(word)
    
    for i in badwords:
        length = len(i)
        inputs = re.sub(r'\b'+i+r'\b','*'*length,inputs)

    return inputs


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
        temp=request.POST.get(i.name,'no value')
        if temp != 'no value':
            selected=selected+','+i.name
    mycategory=selected
    mytitle=request.POST.get('title','no value')
    mycontent=request.POST.get('content','no value')
    mytitle=remove_bad_words(mytitle)
    mycontent=remove_bad_words(mycontent)
    myauthor=request.POST.get('author','no value')
    
    image=request.FILES.get('image','empty')
    video=request.FILES.get('video','empty')
    myflag1=False
    myflag2=False
    if image != 'empty':
        myflag1=True
    if video != 'empty':
        myflag2=True
    # if request.FILES :
    #     image=(request.FILES['image'])
    #     myflag=True
    # else: 
    #     image='empty'
    #     myflag=False
    myid=mytitle+myauthor
    Blog.objects.create(bid=myid,title=mytitle,category=mycategory,content= mycontent,author=myauthor,img=image,vid=video,imgflag=myflag1,vidflag=myflag2)
    return render(request,'postsubmitted.html')
    