from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    path('', views.sign_in_view, name="signin"),
    path('signin', views.sign_in_view, name="signin"),
    path('signup', views.signup_view, name="signup"),
    path('signout', views.signout_view, name="signout"),
]