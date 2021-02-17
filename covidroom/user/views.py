from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm


def index(request):
    return HttpResponse('This is the index page')


def register(request):
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

def login(request):
    pass
