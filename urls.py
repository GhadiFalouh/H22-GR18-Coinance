from django.urls import path
from . import views

#URLCONF
from .Coin import Coin

urlpatterns = [
    path('hello/', views.say_hello),
]