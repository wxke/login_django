from django.shortcuts import render
from app_test import models
# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST.get("Name",None)
        pass1 = request.POST.get("Password1",None)
        pass2 = request.POST.get("Password2",None)
        if pass1 != pass2:
            return render(request, 'index.html',{'ig2':"两次密码不一样"})
        elif models.User.objects.filter(UserName= name).first():
            print(1)
            return render(request,'index.html',{'ig2':"用户已存在"})
        else:
            print(2)
            models.User.objects.create(UserName=name,password=pass1)
            return render(request, 'index.html')
    else:
        return render(request,'index.html')


def home(request):
    if request.method == 'POST':
        name = request.POST.get("Username", None)
        password = request.POST.get("Password", None)
        if models.User.objects.filter(UserName=name,password=password).first():
            return render(request,'home.html',{'name':name})
        else:
            return render(request, 'index.html', {'ig1': "用户名或密码错误"})
    else:
        return render(request, 'index.html')