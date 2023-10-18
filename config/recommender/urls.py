from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.home, name="home"),
    path("home/", views.home, name="home"),
    path("clean/", views.clean, name="clean"),
    path("update/", views.update, name="update"),
    path("recommend/", views.recommend_view, name="recommend"),
    path("signup/", views.signup_page, name="signup"),
    path("login/", views.login_page, name="login"),
    path("logout/", views.logout_view, name="logout")
]
