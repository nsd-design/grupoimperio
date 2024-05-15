from django.contrib import admin
from django.urls import path

from grupo_app import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path('login/', views.login_user, name="login"),
    path('payment/', views.payment, name="payment"),
]
