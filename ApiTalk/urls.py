"""ApitalkBack URL Configuration

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
from django.urls import path
from api import views
urlpatterns = [
    path('Hubble/', views.Hubble.as_view()),
    path('information/', views.information.as_view()),
    path('language/', views.language.as_view()),
    path('mean/', views.mean.as_view()),
    path('median/', views.median.as_view()),
    path('Percentile/', views.Percentile.as_view()),
    path('std/', views.std.as_view()),
    path('TestServerSpeed/', views.TestServerSpeed.as_view()),
    path('var/', views.var.as_view()),
]
