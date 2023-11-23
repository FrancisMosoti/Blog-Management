from django.urls import path
from . import views as my_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', my_views.register, name='register-url'),
    path('login/', my_views.store, name='login-url'),
    path('logout/', my_views.getout, name="logout-url")
]
