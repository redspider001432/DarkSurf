from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
import uuid
from accounts.models import Profile
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'Html/index.html')


def login_attempt(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user_obj = User.objects.filter(username=username).first()
        if user_obj is None:
            messages.success(request, 'User not found')
            return redirect('/login')

        profile_obj = Profile.objects.filter(user=user_obj).first()

        if not profile_obj.isVerified:
            messages.success(request, 'Account is not verified yet')
            return redirect('/login')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('posts')
        else:
            messages.info(request, 'Wrong Password')
            return redirect('login')

    return render(request, 'Html/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST['email']
        password = request.POST['pass1']
        password2 = request.POST['pass2']
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email is already taken')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.set_password(password2)
                auth_token = str(uuid.uuid4())
                user.save()

                user_model = User.objects.get(username=username)
                user_profile = Profile.objects.create(user=user_model, userId=user_model.id, auth_token=auth_token)
                user_profile.save()
                send_register_email(email, auth_token)
                return redirect('token')
        else:
            messages.info(request, 'Password does not match')
            return redirect('register')
    else:
        return render(request, 'Html/register.html')

def success(request):
    return render(request, 'Html/success.html')

def about(request):
    return render(request,'Html/about.html')

def token(request):
    return render(request, 'Html/token.html')

def send_register_email(email, token):
    subject = "Your account need to be verified"
    message = f'Hi paste the link to verify your account https://darksurfnet.herokuapp.com/verify/{token}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)

def verify(request, auth_token):
    try:
        profile_obj = Profile.objects.filter(auth_token=auth_token).first()
        if profile_obj:
            if profile_obj.isVerified is True:
                messages.info(request, 'Account is already verified')
                return redirect('/login')
            profile_obj.isVerified = True
            profile_obj.save()
            messages.success(request, 'Your email verified successfully')
            return redirect('/login')
        else:
            return redirect('/error')
    except Exception as e:
        print(e)

def error(request):
    return render(request, 'Html/error.html')

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect('login')

