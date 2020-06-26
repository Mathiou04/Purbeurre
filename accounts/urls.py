from django.urls import path
from accounts import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.user_login),
    path('logout', views.user_logout),
]
