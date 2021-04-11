from django.shortcuts import render, redirect
from django.http import JsonResponse
from dashboard.database.dbmanager import DBManager
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/signin")
def dashboard(request):
    user = request.user
    all_states = DBManager.get_states()

    if not user.is_admin:
        return redirect("accounts:signin")

    return render(request, "dashboard/dashboard.html", {'all_states': all_states})


def get_chart_data(request):
    selected_state = request.GET['selected_state']
    print(selected_state)

    chart_data = DBManager.get_chart_data(selected_state)
    months = []
    bookings = []
    for item in chart_data:
        mont = item.MONT
        booking = item.BOOKING
        months.append(mont)
        bookings.append(booking)

    data = {}
    data['months'] = months
    data['bookings'] = bookings
    return JsonResponse(data, safe=False)


def get_table_data(request):
    location_data = DBManager.get_location_percent()
    print(location_data)
    return render(request, "dashboard/table1.html", {"location_data": location_data})


def get_pie_graph_data(request):
    selected_state = request.GET['selected_state']
    print(selected_state)

    single_private_room_data = DBManager.get_single_private_room_data(selected_state)
    entire_apt_data = DBManager.get_entire_apt_data(selected_state)
    single_shared_room_data = DBManager.get_single_shared_room_data(selected_state)
    pie_data={}
    pie_data['labels'] = ['Single Private Room', 'Entire Apartment', 'Single Shared Rooms']
    pie_data['data'] = [single_private_room_data, entire_apt_data, single_shared_room_data]
    print(pie_data)
    return JsonResponse(pie_data, safe=False)


def get_table2_data(request):

        best_state = DBManager.get_best_state()
        best_listing = DBManager.get_best_listing()
        best_host = DBManager.get_best_host()
        least_avail = DBManager.get_least_available()
        table2_data = [{"parameter": "Best place to visit", "values": best_state},
                       {"parameter": "Best listing with lowest price per night and highest rating",
                        "values": best_listing},
                       {"parameter": "Host with highest sale", "values": best_host},
                       {"parameter": "Host with most available or least preferred listing", "values": least_avail}]
        print(table2_data)
        return render(request, "dashboard/table2.html", {"table2_data": table2_data})


def get_table3_data(request):
    info_data = DBManager.get_info_table_data()

    data = []
    for item in info_data:
        dict_data = {'name': item.NAME, 'count': item.COUNT}
        data.append(dict_data)


    print(data)
    return render(request, "dashboard/table3.html", {"info_data": data})


def get_chart3(request):
    selected_state = request.GET['selected_state']
    print(selected_state)
    profit = DBManager.get_profit_peryear(selected_state)
    profits = []
    years = []
    for item in profit:
        pr = item.PROFIT
        yr = item.YR
        profits.append(pr)
        years.append(yr)

    chart_data = {}
    chart_data['label'] = years
    chart_data['data'] = profits
    return JsonResponse(chart_data, safe=False)
