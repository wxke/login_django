from django.shortcuts import render,HttpResponse
from app_test import models
import json
# Create your views here.
def index(request):
    dic = {"status": True, "error": ''}
    if request.method == "POST":
        name = request.POST.get("Name",None)
        pass1 = request.POST.get("Password1",None)
        pass2 = request.POST.get("Password2",None)
        print(name,pass1,pass2)
        if models.User.objects.filter(UserName= name).first():
            # return render(request,'index.html',{'ig2':"用户已存在"})
            dic['status'] = False
            dic['error'] = "用户已存在"
            return HttpResponse(json.dumps(dic))
        elif pass1 != pass2:
            dic['status'] = False
            dic['error'] = "两次密码不一样"
            # return render(request, 'index.html',{'ig2':"两次密码不一样"})
            return HttpResponse(json.dumps(dic))
        else:
            models.User.objects.create(UserName=name,password=pass1)
            dic['error'] = "注册成功"
            return HttpResponse(json.dumps(dic))
            # return render(request, 'index.html')
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