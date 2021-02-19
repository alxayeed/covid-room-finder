from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('capacity/', views.get_capacity, name='capacity'),
    path('book/', views.book_room, name='book')
]
