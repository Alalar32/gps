from django.urls import path
from app_staff import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='staff_dashboard'),
]