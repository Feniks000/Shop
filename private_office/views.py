from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

def profile(request):
    return render(request, "profile/profile.html")


@csrf_exempt
def get_massage(request):
    if request.POST:
        print(request.POST.get('withdraw_amount'))
        print(request.POST.get('datetime'))
        print(request.POST.get('label'))
        print(request.POST.get('lastname'))
        print(request.POST.get('firstname'))
        print(request.POST.get('fathersname'))
        print(request.POST.get('sha1_hash'))
        return HttpResponse()
    raise Http404()
