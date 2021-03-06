from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

tripStatus = (
    ("ended", "Ended"),
    ("ongoing", "Ongoing")
)


class Trip (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="trip_check")
    check_in_date = models.DateField(blank=True, null=True)
    check_out_date = models.DateField(blank=True, null=True)
    check_in_time = models.TimeField(blank=True, null=True)
    check_out_time = models.TimeField(blank=True, null=True)
    duration_of_trip = models.PositiveIntegerField(blank=True, null=True)
    amount_paid = models.PositiveIntegerField(blank=True, null=True)
    destination = models.CharField(blank=True, max_length=128, null=True)
    residence_address = models.CharField(blank=True, max_length=128, null=True)
    trip_status = models.CharField(blank=True, max_length=128, null=True, choices=tripStatus)
    car_type = models.CharField(blank=True, max_length=64, null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


def save1(trip, vehicle, tent, equipment, itinerary):
    if trip.trip_status == "ended":
        trip.active = False
        vehicle.active = False
        tent.active = False
        equipment.active = False
        itinerary.active = False

        trip.save()
        vehicle.save()
        tent.save()
        equipment.save()
        itinerary.save()

    if trip.trip_status == "ongoing":
        trip.active = True
        vehicle.active = True
        tent.active = True
        equipment.active = True
        itinerary.active = True

        trip.save()
        vehicle.save()
        tent.save()
        equipment.save()
        itinerary.save()


def my_post_save_handler(sender, instance, **kwargs):
    post_save.disconnect(my_post_save_handler, sender=sender)
    trip = instance
    user = User.objects.get(username=trip.user.username)
    trip = user.trip_check.get(user=user)
    vehicle = user.vehicle_check.get(user=user)
    tent = user.tent_check.get(user=user)# active=True
    equipment = user.equipment_check.get(user=user)
    itinerary = user.itinerary_check.get(user=user)
    save1(trip, vehicle, tent, equipment, itinerary)

    post_save.connect(my_post_save_handler, sender=sender)


post_save.connect(my_post_save_handler, sender=Trip)