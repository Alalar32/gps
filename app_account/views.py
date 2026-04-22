from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator as TokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth import get_user_model

# Create your views here.
token_generator = TokenGenerator()
def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('staff_dashboard') 
        else:
            messages.error(request, 'Invalid username or password. Please try again.')
            return render(request, 'app_account/login.html', {
                'old_data': request.POST,
            })
    
    
    return render(request, 'app_account/login.html')

def register_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confpassword = request.POST.get('confirm_password')
        
        if password != confpassword:
            messages.error(request, 'Passwords do not match. Please try again.')
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different one.')
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already registered. Please use a different email.')
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login')

    return render(request, 'app_account/register.html', {
        'old_data': request.POST,
    })

def logout_view(request):
    logout(request)
    
    # redirect("home")
    return render(request, 'app_public/home.html')

def forgotpassword_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        User = get_user_model()

        user = User.objects.filter(email=email).first()
        if not user:
            messages.error(request, 'No user found with this email address.')
            return redirect('forgot_password')

        token = token_generator.make_token(user)
        uid = urlsafe_base64_encode(force_bytes(user.pk))

        
        # Create reset URL
        reset_url = request.build_absolute_uri(reverse("reset_password", kwargs={"uidb64": uid, "token": token}))

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

def resetpassword_view(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)

    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    
    if user is not None and token_generator.check_token(user, token):
        
        if request.method == "POST":
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')

            if new_password == confirm_password:
                user.set_password(new_password)
                user.save()
                messages.success(request, 'Password reset successful!')
                return redirect('login')
            else:
                messages.error(request, 'Passwords do not match. Please try again.')
    
    return render(request, 'app_account/reset_password.html')

def resetpassword_email_view(request):
    
    return render(request, 'app_account/resetpassword_email.html')
