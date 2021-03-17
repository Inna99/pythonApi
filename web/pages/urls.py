from django.urls import path
from . import views

urlpatterns = [
    path('time/', views.index),
    path('profile/', views.profile),
]
