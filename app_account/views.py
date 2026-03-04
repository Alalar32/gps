from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('staff_dashboard') 
        else:
            return render(request, 'app_account/login.html', {'error': 'Invalid username or password'})
    
    
    return render(request, 'app_account/login.html')

def logout_view(request):
    logout(request)
    
    # redirect("home")
    return render(request, 'app_public/home.html')

def forgotpassword_view(request):
    
    return render(request, 'app_account/forgot_password.html')
