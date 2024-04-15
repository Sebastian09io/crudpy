"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from apps.laptops import views
from apps.laptops.views import principal

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',principal),
    path('registrarCompu/',views.registrar,name='registro'),
    path('vistaed/<int:id>',views.vistaeditar, name='vistae'),
    path('funeditarCompu/<int:id>',views.funcioneditar, name='modificando'),
    path('eliminarcompu/<int:id>',views.eliminar, name='eliminarc'),
    path('vistaprueba/',views.vistaprb,name='vistprb'),
]
