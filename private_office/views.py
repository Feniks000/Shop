from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.contrib.auth import (authenticate,
                                 login as dj_login,
                                 logout as dj_logout)

from .models import Profile, EmailConfirmation, PasswordResetKeys
from django.utils.crypto import get_random_string

from django.core.mail import send_mail
from django.core.mail import *

from shop import settings


@login_required
def profile(request):
    if request.method == 'GET':
        context = {}
        if not request.user.profile.confirmed:
            context['message'] = 'Упс, для начала подтвердите свой аккаунт.'
        return render(request, "private_office/profile.html")
    elif request.method == 'POST':
        pass


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
            context['error'] = True
    return render(request, "private_office/login.html", context)


def logout(request):
    dj_logout(request)
    return redirect('/')


def registration(request):
    context = {}
    if request.method == 'POST':
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        fathersname = request.POST.get('fathersname')
        address = request.POST.get('address')

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username).exists():
            context['error'] = 'Такое имя пользователя уже есть, пожалуйста, выберите другое.'
        # elif (' ', '\t', '\n') in username:
        #     context['error'] = 'Такое имя пользователя недопустимо, пожалуйста, выберите другое.'
        else:
            if password == password2:
                User.objects.create_user(username, email, password)

                user = User.objects.get(username=username)
                user.profile.firstname = firstname
                user.profile.lastname = lastname
                user.profile.fathersname = fathersname
                user.profile.address = address

                key = get_random_string(length=32)
                EmailConfirmation.objects.create(user=user,
                                                 personal_link=key)

                context['message'] = 'Письмо с ссылкой для подтверждения аккаунта ' \
                                     'было отправлено на указанную почту.'
                link = settings.VALIDATION_LINK + email + '/' + key
                user.save()

                status = send_mail('Подтверждение аккаунта',
                                   f'Для подтверждения аккаунта перейдите по этой ссылке: {link}',
                                   settings.EMAIL_HOST_USER,
                                   [email, ],
                                   fail_silently=False)
                print(status)

    return render(request, 'private_office/registration.html', context)


def validation(request, key, email):
    user = get_object_or_404(User,
                             username=get_object_or_404(EmailConfirmation, personal_link=key).user)
    if user.email == email:
        user.profile.confirmed = True
        user.emailconfirmation.delete()

        user.save()
        return render(request, 'private_office/confirmation_page.html')
    else:
        raise Http404()


def resetpassword(request):
    context = {}

    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            context['message'] = 'С такой почтой не зарегистрированно ни одного пользователя'
        else:
            key = get_random_string(length=32)
            PasswordResetKeys.objects.create(user=user,
                                             personal_link=key)

            context['message'] = 'Письмо с ссылкой для сброса пароля ' \
                                 'было отправлено на указанную при регистрации почту.'
            # Я читал про взлом аккаунта если сервер шлет
            # ссылку на введеную почту, а не взятую у юзера
            link = settings.VALIDATION_LINK + email + '/' + key
            user.save()

            status = send_mail('Ссылка для',
                               f'сброса пароля: {link}',
                               settings.EMAIL_HOST_USER,
                               [user.email, ],
                               fail_silently=False)
            print(status)
    return render(request, 'private_office/resetpassword_email.html', context=context)


def accept_resetpassword(request, email, key):
    context = {}
    if request.method == 'GET':
        user = get_object_or_404(User,
                                 username=get_object_or_404(PasswordResetKeys,
                                                            personal_link=key).user)
        if user.email == email:
            return render(request, 'private_office/resetpassword.html', context=context)
        else:
            raise Http404()
    if request.method == 'POST':
        user = get_object_or_404(User,
                                 username=get_object_or_404(PasswordResetKeys,
                                                            personal_link=key).user)
        if user.email == email:
            user.passwordresetkeys.delete()
            user.save()
            context['message'] = 'Аккаунт успешно подтвержден.'
            return render(request, 'private_office/resetpassword.html', context=context)
        else:
            raise Http404()
    raise Http404()


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
