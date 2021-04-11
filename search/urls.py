from django.urls import path
from .views import search_listing


app_name = "search"

urlpatterns = [
    path('', search_listing, name="search")
]