from django.shortcuts import render, get_object_or_404, redirect
from .forms import registerform, itemform
from .models import item
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .filters import itemfilter

# Create your views here.
def register(request):
    if request.method == "POST":
        form = registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = registerform()
    return render(request, "base/register.html", {"form":form})
    
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("home"))
        else:
            return render(request, "base/login.html", {
            "massage": "invalid credentials"
            })
    return render(request, ("base/login.html"))
    

def logout_view(request):
    logout(request)
    return render(request, "base/login.html", {
    "message":"Logged out"
    })


def home(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    good = item.objects.filter(user=request.user).order_by('-id')
    myFilter = itemfilter(request.GET, queryset=good) 
    good = myFilter.qs
    return render(request, ('base/home.html'), {
        'item': good,
        'filter': myFilter
    })

# Create your views here.
def create(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    if request.method == "POST":
        form = itemform(request.POST)
        if form.is_valid():
            names = form.cleaned_data['name']
            dones = form.cleaned_data['done']
            users = request.user
            c = item(user=users, name=names, done=dones)
            c.save()
            return HttpResponseRedirect(reverse("home"))
    else:
        form = itemform()
    return render(request, ('base/create.html'), {
    'form': form
    })
    
def update(request, pk):
    fun = item.objects.get(id=pk)
    fun.done = True
    fun.save()
    return HttpResponseRedirect(reverse("home"))
    
def del_view(request, pk):
    fun = item.objects.get(id=pk)
    fun.delete()
    return HttpResponseRedirect(reverse("home"))
    
def disdate(request, pk):
    fun = item.objects.get(id=pk)
    fun.done = False
    fun.save()
    return HttpResponseRedirect(reverse("home"))