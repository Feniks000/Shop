"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import RedirectView
from django.views.defaults import server_error, page_not_found, permission_denied
from showcase.views import e_handler404, e_handler500, about

urlpatterns = [
    path('home/', include('showcase.urls')),
    path('admin/', admin.site.urls),
    path('about/', about)
]
urlpatterns += [path('accounts/', include('django.contrib.auth.urls')), ]
urlpatterns += [path('', RedirectView.as_view(url='/home/', permanent=True)), ]

# handler403 = curry(permission_denied, template_name='errs/403.html')
handler404 = e_handler404
handler500 = e_handler500

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_STORAGE)
