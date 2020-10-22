from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout as logout_user
from .models import herb
from .form import SearchForm
def index(req):
    return render(req, 'myweb/index.html')
def rog1(req):
    return render(req, 'myweb/rog1.html')
def ro2(req):
    return render(req, 'myweb/ro2.html')
def home1(req):
    return render(req, 'myweb/home1.html')
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'myweb/register.html', {'form': form})

def logout(req):
    logout_user(req)
    return render ('index')

def search(req):
    if req.method == "POST":
        form = SearchForm(req.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            herbs = herb.objects.filter(herb_name__contains=keyword)
        return render(req , "myweb/ro2.html",{"herbs":herbs})
    else:
        form = SearchForm()
        context = {'form':form}
    return render(req, 'myweb/rog1.html',context)