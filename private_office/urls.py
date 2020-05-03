from django.urls import path
from . import views
urlpatterns = [
    path('', views.profile),
    path('messages_afterbuy', views.get_massage)
]