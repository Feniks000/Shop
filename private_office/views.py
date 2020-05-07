from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as dj_login, logout as dj_logout
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User


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
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2:
            User.objects.create_user(username, email, password)
            return redirect(reverse("login"))

    return render(request, 'private_office/registration.html')


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
