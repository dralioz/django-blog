from django.urls import path
from .views import *

global app_name 
app_name = "accounts"

urlpatterns = [

    path("login/", login_view, name="login"),
    path("register/", register_view, name="register"),
    path("logout/", logout_view, name="logout"),
]
