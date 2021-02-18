from django.contrib import admin
from .models import Room, Booking

# Register your models here.


class BookingAdmin(admin.TabularInline):
    model = Booking


class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')
    inlines = [BookingAdmin, ]


admin.site.register(Room, RoomAdmin)
