from django.shortcuts import render, redirect
from django.contrib.auth import login, logout

from accounts.forms import SignInForm, SignUpForm
from accounts.database.dbmanager import DBManager


def sign_in_view(request):
    # generate_booking_data()
    old_user = request.user
    # print(old_user.user_id)
    if not old_user.is_anonymous:
        return redirect("search:search")

    if request.method == "POST":
        sign_in_form = SignInForm(data=request.POST)
        if sign_in_form.is_valid():
            user = sign_in_form.get_user()
            login(request, user)
            if user.is_admin:
                return redirect("dashboard:dashboard")
            else:
                return redirect("search:search")
        else:
            return render(request, "accounts/signin.html", {"form": sign_in_form})
    else:
        sign_in_form = SignInForm()
        return render(request, "accounts/signin.html", {"form": sign_in_form})


def signup_view(request):
    if request.method == "POST":
        sign_up_form = SignUpForm(data=request.POST)

        if sign_up_form.is_valid():
            user = sign_up_form.cleaned_data
            success = DBManager.create_user(user)
            if success:
                return redirect('accounts:signin')
            else:
                sign_up_form.add_error(None,
                                       "This email address is already in use. Please use a different email address.")
                return render(request, "accounts/signup.html", {'form': sign_up_form})
        else:
            return render(request, "accounts/signup.html", {'form': sign_up_form})

    else:
        sign_up_form = SignUpForm()
        return render(request, "accounts/signup.html", {"form": sign_up_form})


def signout_view(request):
    logout(request)
    return redirect("accounts:signin")


# Code To Generate Random Bookings


# listing_ids = ListingDBManager.get_listing_id()
# customer_ids = DBManager.get_customer_id()
#
#
# def generate_booking_data():
#     main_list = []
#     booking_id = 889433
#
#     last_date_string = "1/1/2018"
#     last__date = datetime.datetime.strptime(last_date_string, "%m/%d/%Y")
#
#     check_in_date_string = "1/1/2017"
#     check_in_date = datetime.datetime.strptime(check_in_date_string, "%m/%d/%Y")
#
#     for listing_id in listing_ids:
#         bookings = []
#         while check_in_date < last__date:
#             add_booking = random.choice([True, False])
#
#             if add_booking:         # Add Booking If True
#                 number_of_booking_days = random.randint(1, 10)
#
#                 check_out_date = check_in_date + datetime.timedelta(days=number_of_booking_days)
#                 customer_id = random.choice(customer_ids)
#                 price = (random.randint(100, 500)) * number_of_booking_days
#                 number_of_guests = random.randint(1, 10)
#
#                 booking = Booking(booking_id, listing_id, customer_id, check_in_date, check_out_date,
#                                   price, number_of_guests)
#                 bookings.append(booking)
#
#                 booking_id += 1
#                 check_in_date = check_out_date + datetime.timedelta(days=1)
#             else:
#                 number_of_skipping_days = random.randint(10, 20)
#                 check_in_date = check_in_date + datetime.timedelta(days=number_of_skipping_days)
#
#         main_list.extend(bookings)
#         check_in_date = datetime.datetime.strptime(check_in_date_string, "%m/%d/%Y")
#
#     print("SIZE : "+str(len(main_list)))
#     ListingDBManager.add_booking(main_list)
