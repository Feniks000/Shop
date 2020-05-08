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

from .models import Profile, EmailConfirmation, PasswordResetKeys, Order
from showcase.models import Star
from django.utils.crypto import get_random_string

from django.core.mail import send_mail
from django.core.mail import *
from hashlib import sha1
from shop import settings


@login_required
def profile(request):
    if request.method == 'GET':
        context = {}
        if not request.user.profile.confirmed:
            context['message'] = 'Упс, для начала подтвердите свой аккаунт.'
        all_orders = enumerate(Order.objects.filter(user=request.user))
        data = {
            "orders": list(map(lambda x: (x[0] % 2, x[1]), all_orders)),
        }
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

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if User.objects.filter(username=username).exists():
            context['error'] = 'Такое имя пользователя уже есть, пожалуйста, выберите другое.'
        elif User.objects.filter(email=email).exists():
            context['error'] = 'Аккаунт с такой почтой уже существует!'
        else:
            if password == password2:
                User.objects.create_user(username, email, password)

                user = User.objects.get(username=username)
                user.profile.firstname = firstname
                user.profile.lastname = lastname
                user.profile.fathersname = fathersname

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
            link = settings.RESETPASSWORD_LINK + email + '/' + key
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
            context['message'] = 'Пароль успешно изменен.'
            return render(request, 'private_office/resetpassword.html', context=context)
        else:
            raise Http404()
    raise Http404()


@csrf_exempt
def get_massage(request):
    if request.POST:
        try:
            notification_type = request.POST.get('notification_type')
            withdraw_amount = request.POST.get('withdraw_amount')  # need value
            operation_id = request.POST.get('operation_id')
            unaccepted = request.POST.get('unaccepted')
            sha1_hash = request.POST.get('sha1_hash')
            datetime = request.POST.get('datetime')
            currency = request.POST.get('currency')
            building = request.POST.get('building')
            codepro = request.POST.get('codepro')
            street = request.POST.get('street')
            sender = request.POST.get('sender')
            amount = request.POST.get('amount')
            suite = request.POST.get('suite')
            label = request.POST.get('label')
            city = request.POST.get('city')
            flat = request.POST.get('flat')
            zip = request.POST.get('zip')

            star_id, user_id = label.split('&')
            user = User.objects.get(id=int(user_id))
            star = Star.objects.get(id=int(star_id))
            notification_secret = settings.SECRET_YA_KEY
            my_hash = sha1(f'{notification_type}&'
                           f'{operation_id}&{amount}&{currency}&'
                           f'{datetime}&{sender}&{codepro}&'
                           f'{notification_secret}&{label}'.encode()).hexdigest()

        except Exception:
            raise Exception("HANA OPLATE)))0)")
            # raise Http404()
        else:
            if my_hash == sha1_hash:
                Order.objects.create(
                    user=user,
                    star=star,
                    star_name=star.star_name,
                    withdraw_amount=withdraw_amount,
                    operation_id=operation_id,
                    unaccepted=unaccepted,
                    sha1_hash=sha1_hash,
                    datetime=datetime,
                    currency=currency,
                    building=building,
                    codepro=codepro,
                    street=street,
                    sender=sender,
                    amount=amount,
                    label=label,
                    suite=suite,
                    city=city,
                    flat=flat,
                    zip=zip,
                )
                return HttpResponse()
            else:
                raise Http404()
    raise Http404()
