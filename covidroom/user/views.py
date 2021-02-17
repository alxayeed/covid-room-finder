from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def index(request):
    return HttpResponse('This is the index page')


def register_user(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            form.save()
            return redirect('index')
        else:
            return render(request, 'user/register_form.html', {'form': form})

    return render(request, 'user/register_form.html', {'form': form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponse(f'login successful for {user}')
        else:
            messages.error(request, 'Username or Password is incorrect')
    return render(request, 'user/login.html')
