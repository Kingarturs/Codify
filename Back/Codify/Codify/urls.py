"""Codify URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from rest_framework import routers
from Apps.REST import views as views_REST
from Apps.Accesos import views as views_accesos
from Apps.Documentos import views as views_documentos

router = routers.DefaultRouter()
router.register(r'users', views_REST.UserViewSet)
router.register(r'documentos', views_documentos.DocumentoViewSet)
router.register(r'carpetas', views_documentos.CarpetaViewSet)

urlpatterns = [
    path('rest/', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('token-login/', views_REST.login),
    path('', views_accesos.welcome_view),
    path('login/', views_accesos.login_view),
    path('index/', views_accesos.index_view),
    path('index/crearCarpeta', views_documentos.crearCarpeta),
    path('index/logout', views_REST.logout),
    path('index/codigo', views_documentos.codigo),
    path('index/descargar', views_documentos.descargar),
    path('index/mkdir', views_documentos.mkdir),
    path('index/carpeta', views_documentos.carpeta),
    path('index/archivo', views_documentos.archivo),
    path('index/getCodigo', views_documentos.getCodigo),
]
