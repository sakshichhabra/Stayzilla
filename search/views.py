from django.shortcuts import render, redirect
from .forms import SearchForm
import json
import datetime
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/signin")
def search_listing(request):
    if request.method == 'POST':
        form = SearchForm(data=request.POST)
        if form.is_valid():
            search_query = form.cleaned_data
            json_object = json.dumps(search_query, default=date_converter)
            print(json_object)
            request.session['search_query'] = json_object
            print(search_query)

            return redirect('listing:results')
        else:
            return render(request, 'search/search.html', {"searchform": form})
    else:
        form = SearchForm()
        return render(request, 'search/search.html', {"searchform": form})


def date_converter(o):
    if isinstance(o, datetime.date):

        return o.strftime('%d-%m-%y')


