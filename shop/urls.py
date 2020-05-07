from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView
from django.views.defaults import server_error, page_not_found, permission_denied
from showcase.views import e_handler404, e_handler500, about

urlpatterns = [
    path('home/', include('showcase.urls'), name="home"),
    path('admin/', admin.site.urls, name="admin"),
    path('about/', about, name="about"),
    path('accounts/', include('private_office.urls'), name="accounts"),
    path('^accounts/login/$', LoginView.as_view(), name="login"),
]

urlpatterns += [path('', RedirectView.as_view(url='/home/', permanent=True)), ]
# urlpatterns += [path('accounts/', include('django.contrib.auth.urls')), ]

handler404 = e_handler404
handler500 = e_handler500
