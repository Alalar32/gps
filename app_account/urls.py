from django.urls import path
from app_account import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('forgot-password/', views.forgotpassword_view, name='forgot_password'),
    ]