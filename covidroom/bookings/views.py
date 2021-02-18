from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Room


@login_required(login_url='login')
def index(request):
    print(request.user)
    rooms = Room.objects.all()
    print(rooms)
    context = {
        "rooms": rooms
    }
    return render(request, 'user/index.html', context)
