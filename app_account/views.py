from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings

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

        user = User.objects.filter(email=email).first()

        if not user:
            messages.error(request, 'No user found with this email address.')
            return redirect('forgot_password')

        # Create reset URL
        reset_url = request.build_absolute_uri(reverse("reset_password"))

        # Render email template
        html_content = render_to_string(
            'app_account/resetpassword_email.html',
            {
                "reset_url": reset_url,
                "name": user.first_name or user.username
            }
        )

        try:
            msg = EmailMultiAlternatives(
                'Password Reset Request',
                'Click the link to reset your password.',
                settings.EMAIL_HOST_USER,  
                [email],
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send(fail_silently=False)

            messages.success(request, 'Password reset email sent!')

        except Exception as e:
            print("EMAIL ERROR:", e)  
            messages.error(request, 'Failed to send email. Try again.')
            return redirect('forgot_password')

        

    return render(request, 'app_account/forgot_password.html')

def resetpassword_view(request):
    if request.method == "POST":
        new_password = request.POST.get('new_password')
        confirm_password = request.POST.get('confirm_password')
        current_password = request.POST.get('current_password')

        if new_password == confirm_password:
            user = User.objects.filter(current_password=request.user.password).first()
            user.set_password(new_password)
            user.save()
            
            messages.success(request, 'Password reset successful!')
            return redirect('login')
        else:
            messages.error(request, 'Passwords do not match. Please try again.')
    
    return render(request, 'app_account/reset_password.html')

def resetpassword_email_view(request):
    
    return render(request, 'app_account/resetpassword_email.html')
