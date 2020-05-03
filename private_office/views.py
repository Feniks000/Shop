from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def profile(request):
    return render(request, "profile/profile.html")


def get_massage(request):
    print(request.GET.get('withdraw_amount'))
    print(request.GET.get('datetime'))
    print(request.GET.get('label'))
    print(request.GET.get('lastname'))
    print(request.GET.get('firstname'))
    print(request.GET.get('fathersname'))
    print(request.GET.get('sha1_hash'))
    return HttpResponse()
