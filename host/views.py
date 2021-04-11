from host.database.dbmanager import DBManager
from .forms import HostForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="/accounts/signin")
def host_listing(request):
    user = request.user
    host_id = user.user_id

    if request.method == "POST":
        form = HostForm(data=request.POST)

        if form.is_valid():
            listing = form.cleaned_data
            success = DBManager.create_listing(listing, host_id)
            if success == True:
                return render(request, 'host/confirmation.html')
            else:
                form.errors['DB Error '] = success
                return render(request, "host/host_listing.html", {"form": form})
        else:
            return render(request, "host/host_listing.html", {'form': form})
    else:
        form = HostForm()
        return render(request, "host/host_listing.html", {"form": form})

