from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.models import User

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
    if request.method == "POST":
        email = request.POST.get('email')

        # send_mail("Password Reset Request", "Hello user, you have requested a password reset.", None, [email])
        # return render(request, 'app_account/forgot_password.html', {'message': 'Password reset email sent!'})
        name=User.objects.filter(email=email).first()
        if not name:
            return render(request, 'app_account/forgot_password.html', {'error': 'No user found with this email address.'})
        
        # 1. Create email
        reset_url = request.build_absolute_uri(reverse("reset_password"))
        html_content = render_to_string(
            'app_account/resetpassword_email.html',
            {"reset_url": reset_url, "name": name.first_name or name.username},
        )
        
        msg = EmailMultiAlternatives(
                'Password Reset Request',
                'Hello user, you have requested a password reset.',
                None,
                [email],
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()

       
        return render(request, 'app_account/forgot_password.html', {'message': 'Password reset email sent!'})

        

    return render(request, 'app_account/forgot_password.html')

def resetpassword_view(request):
    if request.method == "POST":
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')

        if new_password == confirm_password:
            #i will write the logic to change the password later 
            messages.success(request, 'Password reset successful!')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')
    
    return render(request, 'app_account/reset_password.html')

def resetpassword_email_view(request):
    
    return render(request, 'app_account/resetpassword_email.html')
