from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.urls import reverse

from django.contrib.auth.models import User

from .models import Profile, EmailConfirmation
from django.utils.crypto import get_random_string

from django.contrib.auth import password_validation
from django.core.mail import send_mail
from django.core.mail import *
from shop import settings


# Create your views here.

def profile(request):
    return render(request, "private_office/profile.html")


def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dj_login(request, user)
            return redirect("/")
        else:
            context['error'] = "Логин или пароль неправильные"
    return render(request, "private_office/login.html", context)


def logout(request):
    dj_logout(request)
    return redirect('/')


def registration(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username).exists():
            context['error'] = 'Такое имя пользователя уже есть,<br>' \
                               'пожалуйста, выберите другое.'
        else:
            if password == password2:
                User.objects.create_user(username, email, password)
                key = get_random_string(length=32)
                EmailConfirmation.objects.create(user=User.objects.get(username=username),
                                                 personal_link=key)

                context['message'] = 'Письмо с ссылкой для подтверждения аккаунта<br>' \
                                     'было отправлено на указанную почту.'
                link = settings.VALIDATION_LINK + '/' + email + '/' + key
                status = send_mail('Подтверждение аккаунта',
                                   f'Для подтверждения аккаунта перейдите по этой ссылке: {link}',
                                   'noreply@starshop25.com',
                                   [email, ],
                                   fail_silently=False)
                print(status)

    return render(request, 'private_office/registration.html', context)


def validation(request, key, email):
    user = get_object_or_404(User,
                             username=get_object_or_404(EmailConfirmation, personal_link=key).user)

    if user.email == email:
        return HttpResponse("Успех.")
    else:
        return HttpResponse("Провал")


@csrf_exempt
def get_massage(request):
    secret = 'xlob6eQOzV74hIYRTZFec5Ov'
    if request.POST:
        print(request.POST.get('withdraw_amount'))
        print(request.POST.get('datetime'))
        print(request.POST.get('label'))
        print(request.POST.get('lastname'))
        print(request.POST.get('firstname'))
        print(request.POST.get('fathersname'))
        print(request.POST.get('sha1_hash'))
        # print(request.POST.get(''))
        return HttpResponse()
    raise Http404()
