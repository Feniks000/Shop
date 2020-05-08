from django.urls import path
from . import views

urlpatterns = [
    path('profile', views.profile, name="profile"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('messages_afterbuy', views.get_massage),
    path('register', views.registration, name="registration"),
    path('validation/<str:email>/<str:key>', views.validation),  # it used in registration
    path('resetpassword/accept/<str:email>/<str:key>', views.accept_resetpassword),  # second
    path('resetpassword$', views.resetpassword, name="resetpassword"),  # first
]
