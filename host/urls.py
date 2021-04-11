from django.urls import path
from . import views

app_name = "host"

urlpatterns = [
    path('',views.host_listing, name="host"),
]


