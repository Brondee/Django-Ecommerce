from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import Register

# Create your views here.
def user_register(response):
    if response.method == "POST":
        form = Register(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/login/")
    else:
        form = Register()

    return render(response, 'register/register.html', {"form":form})
