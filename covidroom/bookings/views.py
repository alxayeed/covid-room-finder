from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Room, Booking
from .forms import BookingForm
from django.forms import ValidationError


@login_required(login_url='login')
def index(request):
    rooms = Room.objects.all()
    context = {
        "rooms": rooms
    }
    return render(request, 'user/index.html', context)


def get_capacity(request):
    "Get current Empty Capacity of all rooms"

    date = request.POST.get('date')
    total_capacity = 0
    total_vacant = 0
    for room in Room.objects.all():
        total_capacity += room.capacity
        total_vacant += (room.capacity - len(room.booking.filter(date=date)))
    current_vacancy = (total_vacant / total_capacity) * 100

    rooms = Room.objects.all()

    context = {
        'rooms': rooms,
        'date': date,
        'vacancy': f'{current_vacancy:.2f}'
    }

    return render(request, 'user/index.html', context)


def book_room(request):
    form = BookingForm(request.POST)

    room = request.POST.get('room')
    date = request.POST.get('date')
    name = request.POST.get('name')
    username = request.POST.get('username')

    current_room = Room.objects.get(name=room)
    current_bookings = len(current_room.booking.filter(date=date))

    if current_bookings < current_room.capacity:
        Booking.objects.create(
            room=current_room,
            username=username,
            fullname=name,
            date=date
        )
    else:
        bookers = []
        for booking in current_room.booking.filter(date=date):
            bookers.append(booking.fullname)

        rooms = Room.objects.all()
        room_info = {}
        for room in rooms:
            empty = room.capacity - len(room.booking.filter(date=date))
            if empty > 0:
                room_info[room.name] = empty

        context = {
            'current_room': current_room,
            'bookers': bookers,
            "rooms": rooms,
            "room_info": room_info
        }
        return render(request, 'user/index.html', context)

    return redirect('/')


def get_bookings(request):
    all_bookings = Booking.objects.filter(username=request.user)
    rooms = Room.objects.all()

    context = {
        'rooms': rooms,
        'all_bookings': all_bookings
    }
    return render(request, 'user/index.html', context)


def delete_booking(request, id):
    Booking.objects.filter(pk=id).delete()

    return redirect('bookings')
