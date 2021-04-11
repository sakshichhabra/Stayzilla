from .database.dbmanager import DBManager
from django.http import JsonResponse


def get_popularity_trend(request):
    listing_id = request.GET['listing_id']
    bookings = DBManager.get_popularity_trend(listing_id)
    months = []
    values = []

    for booking in bookings:
        month = booking.MONTH
        value = booking.BOOKINGS

        months.append(month)
        values.append(value)

    chart_data = {}
    chart_data['months'] = months
    chart_data['values'] = values

    return JsonResponse(chart_data, safe=False)


def get_price_trend(request):
    listing_id = request.GET['listing_id']
    bookings = DBManager.get_monthly_price_trend(listing_id)
    months = []
    prices = []

    for booking in bookings:
        month = booking.MONTH
        price = booking.PRICE

        months.append(month)
        prices.append(price)

    chart_data = {}
    chart_data['months'] = months
    chart_data['prices'] = prices

    return JsonResponse(chart_data, safe=False)
