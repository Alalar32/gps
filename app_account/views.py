from django.shortcuts import render

# Create your views here.
def login_view(request):
    return render(request, 'app_account/login.html')
def forgotpassword_view(request):
    return render(request, 'app_account/forgot_password.html')
