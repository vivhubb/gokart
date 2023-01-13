from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='race-home'),
    path('feedback/', views.feedback, name='race-feedback'),
    path('booking/', views.booking, name='race-booking'),
]
