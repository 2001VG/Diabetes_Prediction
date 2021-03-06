"""DiabetesPrediction URL Configuration

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
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("" , views.diabetes),
    path("diabetes/", views.diabetes),
    path("about/", views.about),
    path("register/" , views.register),
    path("register/diabetes/" , views.diabetes),
    path("about/diabetes/", views.diabetes),
    path('login/diabetes/' ,views.diabetes),
    path('login/' , views.login),
    path('predict/' , views.predict),
    path('register/login/' , views.login),
    path('login/predict/', views.predict),
    path('login/predict/Outcome', views.outcome),
    path('login/predict/diabetes/',views.diabetes),
    path('register/login/diabetes/', views.diabetes),
    path('register/login/predict/' , views.predict),
    path('register/login/predict/diabetes/' , views.diabetes)
]
