from django.db import models


class Room(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name


class Booking(models.Model):
    room = models.ForeignKey(
        Room, on_delete=models.CASCADE, related_name='booking')
    username = models.CharField(max_length=20)
    fullname = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.fullname
