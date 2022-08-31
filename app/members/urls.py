import imp
from django.urls import path, include
from .views import login_view, logout_view, register_view

app_name = 'members'

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('register/', register_view, name="register"),
    path('logout', logout_view, name="logout"),
    path('login', login_view, name="login"),
]
