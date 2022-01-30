"""POTENCIAS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from paypa import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="home"), 
    path('Quiromancia/', views.Quiromancia, name="Quiromancia"),
    path('Pagos/', views.Pagos, name="Pagos"),
    path('Servicios/', views.Servicios, name="Servicios"),
    path('Tarot/', views.Tarot, name="Tarot"),
    path('Membresias/', views.Membresias, name="Membresias"),
    path('Horoscopo/', views.Horoscopo, name="Horoscopo"),
    path('Contacto/', views.Contacto, name="Contacto"),
    path('Historia/', views.Historia, name="Historia"),
    path('', include('paypa.urls')),
]
if settings.DEBUG:
   #from django.conf.urls.static import static
   urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) 