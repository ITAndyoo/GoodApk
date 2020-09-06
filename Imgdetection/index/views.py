from django.shortcuts import render
from django.http import HttpResponse

def getlogin(request):
        return render(request,'login.html')

def getindex(request):
    if request.method == 'GET' :
        return render(request,'index.html')
    else:
        if request.POST["username"] == "admin" and request.POST["password"] == "123" :
            return render(request,'index.html')
        else :
            return HttpResponse("用户名或密码错误！")


# Create your views here.
