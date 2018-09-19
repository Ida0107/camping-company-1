from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from search.models import Search
from destination.models import Destination
from itinerary.models import Itinerary
import requests

# Create your views here.


# def destination(request):
#     return render(request, "customer/destination.html")


@login_required
def user_page(request):
    Search.objects.new_or_get(request)
    items = Destination.objects.all()
    context = {"items": items}
    return render(request, "customer/destination.html", context)


@login_required
def user_detail_page(request, pk):
    Search.objects.new_or_get(request)
    item = Destination.objects.get(pk=pk)
    context = {"item": item}
    return render(request, "customer/detail.html", context)


@login_required
def custom_itinerary(request):
    data = Itinerary.objects.filter(user=request.user, active=True)
    list1 = []
    list2 = []
    hour = 12
    for x in data:
        for y in x.destination.all():
            if hour-y.hours >= 0:
                list2.append(y.pk)
                hour = hour - y.hours
            else:
                list1.append(list2)
                list2 = []
                list2.append(y.pk)
                hour = 12
        list1.append(list2)

    if request.is_ajax():
        message = request.POST.get("places")
        list1 = [int(s) for s in message.split(',')]
        itinerary = Itinerary(user=request.user)
        itinerary.save()
        for x in list1:
            destination = Destination.objects.get(pk=x)
            itinerary.destination.add(destination)
    return render(request, "customer/custom.html", {"data": data, "list": list1})


@login_required
def book(request, pk):
    # user = User.objects.get(pk=pk)
    # email = str(user.email)
    # name = str(user.first_name)
    # subject = str("Booking")
    # message = str("{} just Booked a car :D name {} phone {}".format(name, user.first_name, user.customer_check.phone))
    # simple_message(name, email, subject, message)
    return render(request, "customer/success.html")
