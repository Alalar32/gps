from django.urls import path
from app_account import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('forgot-password/', views.forgotpassword_view, name='forgot_password'),
    path('reset-password/',views.resetpassword_view, name="reset_password"),
    path('reset-password-email/',views.resetpassword_email_view, name="reset_password_email"),
    ]
