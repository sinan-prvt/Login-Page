from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages
from django.db import IntegrityError

# Create your views here.
def index(request):
    return render(request, 'index.html')

def loginn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, f"Welcome back, {username}! 🎉")
            return redirect('home')
        else :
            messages.error(request, "Invalid username or password ❌")
            return redirect("register")
    return render(request, "login.html")


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            myuser = User.objects.create_user(username=username, email=email, password=password)
            myuser.save()
            messages.success(request, "✅ Account created successfully! Please log in.")
            return redirect('login')
        except IntegrityError:
            messages.error(request, "⚠️ Username already exists. Please try again.")
            return redirect('register')
    return render(request, 'register.html')

def home(request):
    return render(request, 'home.html')