from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from vehicle.models import VehicleCheck
from search.models import Search
from django.utils.dateparse import parse_date

# Create your views here.

def vehicles(request):
    #if request.method == "POST":
     #   city = request.POST.get("place")
       # tripDay = parse_date(request.POST.get("tripDay"))
      #  totalDays = request.POST.get("Duration")
        #if city == "" or tripDay == "" or totalDays is None:
         #   city = None
          #  tripDay = None
           # totalDays = None

        #Search.objects.new_or_get(request, city=city, tripDay=tripDay, totalDays=totalDays)
    return render(request, "vehicle/vehicles.html")


def thar(request):
    return render(request, "vehicle/vehicle1.html")


def vehicle_info(request):
    return render(request, "vehicle/vehicle_info.html")


def time(request):
    return render(request, "vehicle/vehicle2.html")


def vehicle_create_check(request, pk):
    if request.method == "POST":
        users = User.objects.get(pk=pk)
        engine_oil_level = request.POST.get("brake_fluid")
        brake_fluid_level = request.POST.get("water_level")
        water_level = request.POST.get("brake_fluid")
        windscreen_washer = request.POST.get("windscreen")
        seatbelts_check = request.POST.get("seatbelts")
        parking_brake = request.POST.get("parking")
        clutch_gearshift = request.POST.get("clutch")
        burning_smell = request.POST.get("burning")
        steering_alignment = request.POST.get("steering")
        dashboard = request.POST.get("dashboard")
        check_lights = request.POST.get("check_lights")
        horn = request.POST.get("horn")
        tyres = request.POST.get("tyres")
        leakage = request.POST.get("leakage")

        VehicleCheck.objects.get_or_create(user=users, engine_oil_level=engine_oil_level,
                                           brake_fluid_level=brake_fluid_level, water_level=water_level,
                                           windscreen_washer=windscreen_washer, seatbelts_check=seatbelts_check,
                                           parking_brake=parking_brake, clutch_gearshift=clutch_gearshift,
                                           burning_smell=burning_smell, steering_alignment=steering_alignment,
                                           dashboard=dashboard, check_lights=check_lights, horn=horn, tyres=tyres,
                                           leakage=leakage)

        return redirect("app:create_status", pk=users.pk)

    else:
        return render(request, "vehicle/vehicle_create_check.html")


def vehicle_update_check(request, pk):
    vehicle = VehicleCheck.objects.get(pk=pk, active=True)
    if request.method == "POST":
        users = User.objects.get(pk=vehicle.user.pk)
        engine_oil_level = request.POST.get("brake_fluid")
        brake_fluid_level = request.POST.get("water_level")
        water_level = request.POST.get("brake_fluid")
        windscreen_washer = request.POST.get("windscreen")
        seatbelts_check = request.POST.get("seatbelts")
        parking_brake = request.POST.get("parking")
        clutch_gearshift = request.POST.get("clutch")
        burning_smell = request.POST.get("burning")
        steering_alignment = request.POST.get("steering")
        dashboard = request.POST.get("dashboard")
        check_lights = request.POST.get("check_lights")
        horn = request.POST.get("horn")
        tyres = request.POST.get("tyres")
        leakage = request.POST.get("leakage")

        VehicleCheck.objects.update(user=users, engine_oil_level=engine_oil_level,
                                    brake_fluid_level=brake_fluid_level, water_level=water_level,
                                    windscreen_washer=windscreen_washer, seatbelts_check=seatbelts_check,
                                    parking_brake=parking_brake, clutch_gearshift=clutch_gearshift,
                                    burning_smell=burning_smell, steering_alignment=steering_alignment,
                                    dashboard=dashboard, check_lights=check_lights, horn=horn, tyres=tyres,
                                    leakage=leakage)

        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "vehicle/vehicle_update_check.html", {"vehicle": vehicle})
