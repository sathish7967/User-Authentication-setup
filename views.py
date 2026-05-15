from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail

from .models import User
from .utils import generate_otp
from django.contrib.auth import logout


# LOGIN VIEW
def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.role == 'admin':
                return redirect('admin_dashboard')

            elif user.role == 'distributor':
                return redirect('distributor_dashboard')

        else:
            return render(request, 'login.html', {
                'error': 'Invalid Credentials'
            })

    return render(request, 'login.html')


# ADMIN DASHBOARD
def admin_dashboard(request):
    return render(request, 'admin_dashboard.html')


# DISTRIBUTOR DASHBOARD
def distributor_dashboard(request):
    return render(request, 'distributor_dashboard.html')


# FORGOT PASSWORD
def forgot_password(request):

    if request.method == 'POST':

        email = request.POST['email']

        try:
            user = User.objects.get(email=email)

            otp = generate_otp()

            user.otp = otp
            user.save()

            send_mail(
                'Password Reset OTP',
                f'Your OTP is {otp}',
                'admin@example.com',
                [email],
                fail_silently=False,
            )

            return redirect('verify_otp')

        except:
            return render(
                request,
                'forgot_password.html',
                {'error': 'Email not found'}
            )

    return render(request, 'forgot_password.html')


# VERIFY OTP
def verify_otp(request):

    if request.method == 'POST':

        email = request.POST['email']
        otp = request.POST['otp']

        try:
            user = User.objects.get(email=email)

            if user.otp == otp:
                return redirect('reset_password')

            else:
                return render(
                    request,
                    'verify_otp.html',
                    {'error': 'Invalid OTP'}
                )

        except:
            pass

    return render(request, 'verify_otp.html')


# RESET PASSWORD
def reset_password(request):

    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.get(email=email)

        user.password = make_password(password)
        user.otp = None
        user.save()

        return redirect('login')

    return render(request, 'reset_password.html')


# LOGOUT
def user_logout(request):

    logout(request)

    return redirect('login')
