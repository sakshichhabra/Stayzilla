from django.urls import path
from .views import search_result, get_details, get_reviews, get_past_prices, get_future_prices,search_filter_result,search_popular_result
from .api import get_popularity_trend, get_price_trend

app_name = "listing"

urlpatterns = [
    path('details/<int:listing_id>', get_details, name="details"),
    path('result/', search_result, name="results"),
    path('filter/<int:price>',search_filter_result,name="filter"),
    path('score/<int:score>',search_popular_result,name="score"),
    path('review/data', get_reviews, name='review-data'),
    path('popularity/data', get_popularity_trend, name='popularity-data'),
    path('price/data', get_price_trend, name='price-data'),
    path('past/price/data', get_past_prices, name='past-price-data'),
    path('future/price/data', get_future_prices, name='future-price-data'),
]