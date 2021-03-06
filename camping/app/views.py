from django.shortcuts import render, redirect, Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from trip.models import Trip
from destination.models import Destination

import requests

# Create your views here.

def home(request):
    return render(request, "app/home.html")


def about(request):
    return render(request, "app/about.html")


def terms_condition(request):
    return render(request, "app/terms_condition.html")


def calender(request):
    if request.user.is_superuser:
        x = Trip.objects.filter(trip_status="ongoing")
        y = Trip.objects.filter(trip_status="ongoing")

        for thar in x:
            thar = thar

        for xenon in y:
            xenon = xenon

        if x.count() == 1 and y.count() == 1:
            context = {
                "thar": thar,
                "Xenon": xenon
            }
        else:
            raise Http404("You Did not have save previous trips as ended please fix and try again")

        return render(request, "app/calender.html", context)

    else:
        return redirect("customer:user_page")


def findus(request):
    if request.method == "POST":
        email = str(request.POST.get("email"))
        name = str(request.POST.get("name"))
        subject = str(request.POST.get("subject"))
        message = str(request.POST.get("message"))
        # simple_message(name, email, subject, message)
        return redirect("findus")
    else:
        return render(request, "app/findus.html")


@login_required
def find_user(request):
    if request.user.is_superuser:
        if request.method == "POST":
            email = request.POST.get("email")
            try:
                users = User.objects.get(email=email)
            except User.DoesNotExist:
                raise Http404("User does not exist")

            return render(request, "app/find_user.html", {"users": users})
        else:
            return render(request, "app/find_user.html")
    else:
        return redirect("customer:user_page")


@login_required
def create_status(request, pk):
    if request.user.is_superuser:
        users = User.objects.get(pk=pk)
        return render(request, "app/create_check.html", {"users": users})
    else:
        return redirect("customer:user_page")


@login_required
def show_status(request, pk):
    if request.user.is_superuser:
        users = User.objects.get(pk=pk)
        trip = users.trip_check.filter(user=users, active=True)
        if trip.count() == 1:
            return render(request, "app/show.html", {"users": users, "active": True})
        else:
            return render(request, "app/show.html", {"users": users, "active": False})

    else:
        return redirect("customer:user_page")


@login_required
def represent(request):
    if request.user.is_superuser:
        return render(request, "app/represent.html")
    else:
        return redirect("customer:user_page")


def destination(request):
    items = Destination.objects.all()
    return render(request, "app/destination.html", {"items": items})


