from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Star
from shop.settings import MEDIA_URL


# Create your views here.

def index(request):
    all_stars = enumerate(Star.objects.all())
    data = {
        "stars": list(map(lambda x: (x[0] % 2, x[1]), all_stars)),
        "MEDIA_URL": MEDIA_URL,
    }
    return render(request, 'showcase/index.html', data)


def show_product(request, star_id):
    obj = get_object_or_404(Star, id=star_id)
    data = {"star": obj,
            "MEDIA_URL": MEDIA_URL}
    # return HttpResponse(f'<img src="{MEDIA_URL}{obj.img()}">')
    return render(request, 'showcase/product.html', data)


def buy(request):
    obj = get_object_or_404(Star, id=request.GET.get('id'))
    data = {
        "star": obj
    }
    return render(request, 'showcase/buy.html', data)
