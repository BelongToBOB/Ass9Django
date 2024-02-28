from django.urls import path
from myapp import views

urlpatterns = [
    path('index',views.index),
    path('about',views.about),
    path('form',views.form),
    path('interest',views.interest),
    path('idol',views.idol),
    path('',views.home),
]