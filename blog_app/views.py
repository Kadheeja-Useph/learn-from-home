from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from . models import Blog
from django.contrib.auth.models import User,auth
from django.shortcuts import redirect
from django.contrib import messages

def index(request):
    blog= Blog.objects.all()
    argument = {
        'name':'Kadheeja',
        'blog':blog,
    }
    return render(request,'index.html',argument)
def slug(request,slug):
    blog= Blog.objects.filter(slug=slug)
    argument = {
        'name':'Kadheeja',
        'blog':blog,
    }
    return render(request,'blog-template.html',argument)

def dashboard(request):
    blog= Blog.objects.all()
    argument = {
        'blog':blog,
    }
    return render(request,'dashboard.html',argument)
def login(request):
    if request.method == "POST":
        username = request.POST['userid']
        password = request.POST['password']
        User = auth.authenticate(username=username,password=password)
        if User is not None:
            auth.login(request,User)
            print("loged in")
            return redirect('/dashboard')
        else:
            messages.error(request,"invalid entry")
            return redirect('/login')
    else:
        return render(request,'login.html')
def logout(request):
    auth.logout(request)
    return redirect('/')
def add(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        slug = request.POST['slug']
        blog_add = Blog(title=title,body=body,slug=slug)
        blog_add.save()
        return redirect('/dashboard')
    else:
        return render(request,'add.html')
def delete(request):
    if request.method == "POST":
        blog_id = request.POST['id']
        Blog.objects.filter(id=blog_id).delete()
        return redirect('/dashboard')
    else:
        return render(request,'add.html') 
def update(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        slug = request.POST['slug']
        blog_id = request.POST['id']
        Blog.objects.filter(id=blog_id).update(title=title,body=body,slug=slug)
        return redirect('/dashboard')
    else:
        return render(request,'update.html')
def id(request,id):
    blog= Blog.objects.filter(id=id)
    argument = {
        'name':'Kadheeja',
        'blog':blog,
    }
    return render(request,'update.html',argument)
