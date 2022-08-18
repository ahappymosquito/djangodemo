from django.shortcuts import render,HttpResponse,redirect
from app.models import userinfo

# Create your views here.
def index(request):
    return HttpResponse("hello,world")

def user(request):
    return render(request,"user_list.html")

def orm(request):
    # 新建
    userinfo.objects.create(name='kldxwz',age=19)
    # 删除
    # userinfo.objects.all().delete()
    # userinfo.objects.filter(age=19).delete()
    return HttpResponse("DONE")

def show_list(request):
    if request.method == "GET":
        id =request.GET.get('id')
        userinfo.objects.filter(id=id).delete()
        data = userinfo.objects.all()
        return render(request,'show.html', {"data" :data})
    if request.method == "POST":
        usr=request.POST.get("user")
        age = request.POST.get("age")
        userinfo.objects.create(name=usr,age=age)
        return redirect("/show")

def demo(request):
    name =  "kldxwz"
    list1 = ["a","b"]
    return render(request,"demo.html",{"a":name,"b":list1})