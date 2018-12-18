from django.shortcuts import render,HttpResponse,redirect
from app_test import models
import json
import os
from django.views.decorators.csrf import csrf_exempt,csrf_protect #csfr_exempt 让其没有csrf保护 csrf_protect  让它有
# Create your views here.
def index(request):
    dic = {"status": True, "error": ''}
    if request.method == "POST":
        name = request.POST.get("Name",None)
        pass1 = request.POST.get("Password1",None)
        pass2 = request.POST.get("Password2",None)

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
            # obj = render(request,'home.html',{'name':name})
            # obj.set_cookie('username',name,max_age=6)
            # return obj
            request.session['username'] = name
            request.session['password'] = password
            request.session['is_login'] = True
            request.session.set_expiry(0)
            return render(request,'home.html',{'name':name})
        else:
            return render(request, 'index.html', {'ig1': "用户名或密码错误"})
    elif request.method == 'GET':
        print("33")
        if request.session['is_login'] == True:
            print("11")
            return render(request,'home.html',{'name':request.session['username']})
        else:
            return redirect('/index')
        # if request.COOKIES.get('username'):
        #     return render(request,'home.html',{'name':request.COOKIES.get('username')})
        # return redirect('/index')

def manage(request):
    if request.method == 'POST':

        title1 = request.POST.get('title1',None)
        auth = request.POST.get('auth1',None)
        file1 = request.FILES.get('file',None)
        user = request.POST.get('user',None)
        password = request.POST.get('password',None)
        type_user = request.POST.get('type_user',None)
        if title1 != None and auth != None and file1 != None:
            models.Book.objects.create(BookName=title1,auth=auth)
            dir_file = open(os.path.join('C:\\Users\\wxk\\Desktop\\upload', file1.name), 'wb+')
            for chunk in file1.chunks():
                dir_file.write(chunk)
        if user != None and password != None and type_user != None:
            models.User.objects.create(UserName=user,password=password)
        return render(request, "manage.html",{'name':request.session['username']})
    elif request.method == 'GET':
        if request.session['is_login'] == True:
            book_name = request.GET.get('book_name', None)
            username = request.GET.get('username', None)
            if book_name != None:
                book = models.Book.objects.filter(BookName__icontains=book_name)
                str1 = ''
                cont = 1
                for i in book:
                    str1 += '<tr><th scope="row">'+str(cont)+'</th><td>'+i.BookName+'</td><td>'+i.auth+'</td><td>'+str(i.date)+'</td></tr>'
                    cont +=1
                return HttpResponse(str1)
            elif username != None:
                use = models.User.objects.filter(UserName__icontains=username)
                str1 = ''
                cont = 1
                for i in use:
                    str1 += '<tr><th scope="row">'+str(cont)+'</th><td>'+i.UserName+'</td><td>'+i.password+'</td><td>'+str(i.user_type)+'</td></tr>'
                    cont +=1
                return HttpResponse(str1)

            else:
                book = models.Book.objects.all()
                str1 = ''
                cont = 1
                for i in book:
                    str1 += '<tr><th scope="row">' + str(cont) + '</th><td>' + i.BookName + '</td><td>' + i.auth + '</td><td>' + str(i.date) + '</td></tr>'
                    cont += 1
                use = models.User.objects.all()
                str2 = ''
                cont = 1
                for i in use:
                    str2 += '<tr><th scope="row">' + str(cont) + '</th><td>' + i.UserName + '</td><td>' + i.password + '</td><td>' + str(i.user_type) + '</td></tr>'
                    cont += 1
                return render(request,'manage.html',{'str1':str1,'str2':str2,'name':request.session['username']})
        else:
            return redirect('/index')


def cancel(request):
    request.session['is_login'] = False
    return redirect('/index')

def test(request):
    return HttpResponse(request)