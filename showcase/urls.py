from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('login/', include('private_office.urls')),
    path('<int:star_id>/', views.show_product),
    path('buy/', views.buy)
]
