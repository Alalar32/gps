from django.urls import path
from app_public import views

urlpatterns = [
    path('', views.home, name='home'),
]