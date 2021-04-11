from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .database.dbmanager import DBManager
from search.database.dbmanager import DBManager as SearchManager
from booking.forms import BookingForm
from booking.models import Booking
import json


@login_required(login_url="/accounts/signin")
def search_result(request):

    search_query = request.session.get('search_query')
    json_query = json.loads(search_query)
    city = json_query.get('destination')
    print(search_query)
    listings = SearchManager.search_customer_listing(json_query)
    print(listings)
    return render(request, 'listing/result.html', {"listings": listings,
                                                   "city": city})

@login_required(login_url="/accounts/signin")
def search_filter_result(request,price):
    print("Reached filter")
    search_query = request.session.get('search_query')
    json_query = json.loads(search_query)
    city = json_query.get('destination')

    print(search_query)
    listings = SearchManager.search_price_filtered_listing(json_query,price)
    # print(listings)
    return render(request, 'listing/result.html', {"listings": listings,
                                                   "city": city})

@login_required(login_url="/accounts/signin")
def search_popular_result(request,score):
    print("Reached filter")
    print(score)
    search_query = request.session.get('search_query')
    json_query = json.loads(search_query)
    city = json_query.get('destination')

    print(search_query)
    listings = SearchManager.search_score_filtered_listing(json_query,score)
    # print(listings)
    return render(request, 'listing/result.html', {"listings": listings,
                                                   "city": city})

@login_required(login_url="/accounts/signin")
def get_details(request, listing_id):
    user = request.user
    search_query = request.session.get('search_query')
    json_query = json.loads(search_query)

    available_dates_with_price = DBManager.get_available_dates_with_price(listing_id)
    listing = DBManager.get_listing_for_id(listing_id)
    best_time = DBManager.get_best_time_to_visit(listing_id)

    check_in_string = json_query.get('from_date')
    check_out_string = json_query.get('to_date')

    dict_dates = {'check_in': check_in_string,
                  'check_out': check_out_string,
                  'available_dates_with_price': available_dates_with_price}

    if request.method == "POST":
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.cleaned_data
            success = DBManager.add_booking(booking)
            if success == True:
                return render(request, 'listing/confirmation.html', {'listing': listing})
            else:
                booking_form.errors['DB Error '] = success
        return render(request, 'listing/details/details.html', {
                                                        'listing': listing,
                                                        'booking_form': booking_form,
                                                        'dict_dates': dict_dates,
                                                        'best_time': best_time})
    else:
        booking = Booking()
        booking.customer_id = user.user_id
        booking.listing_id = listing_id
        booking.number_of_guests = json_query.get('num_guests')
        booking.price = 0
        booking_form = BookingForm(instance=booking)

        return render(request, 'listing/details/details.html', {'listing': listing,
                                                                'booking_form': booking_form,
                                                                'dict_dates': dict_dates,
                                                                'best_time': best_time})


def get_reviews(request):
    listing_id = request.GET['listing_id']
    reviews = DBManager.get_reviews(listing_id)
    return render(request, "listing/details/reviews.html", {"reviews": reviews})


def get_past_prices(request):
    listing_id = request.GET['listing_id']
    date_string = request.GET['date']
    prices = DBManager.get_past_weekly_price_trend(listing_id, date_string)
    return render(request, "listing/details/prices.html", {"prices": prices})


def get_future_prices(request):
    listing_id = request.GET['listing_id']
    date_string = request.GET['date']
    prices = DBManager.get_future_weekly_price_trend(listing_id, date_string)
    return render(request, "listing/details/prices.html", {"prices": prices})
