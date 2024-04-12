from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from .models import User
# Create your views here.

def signup(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        password1 = request.POST.get("password1", "")
        password2 = request.POST.get("password2", "")

        if password1 == password2 and name and email and password1 and password2:
            user = User.objects.create_user(name, email, password1)
            return redirect("/login/")
        else:
            print("Something went wrong!")
    return render(request, "signup.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        if email and password:
            user = authenticate(request, email=email, password = password)
            if user is not None:
                auth_login(request, user)
                return redirect("/")
            

    return render(request, "login.html")


def template(request):
    return render(request, "template.html")

def logout(request):
    auth_logout(request)
    return redirect("/login")