from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from tent.models import TentCheck

# Create your views here.


def tent_create_check(request, pk):
    if request.method == "POST":
        user = User.objects.get(pk=pk)
        rod = request.POST.get("rod")
        mattress = request.POST.get("mattress")
        zip = request.POST.get("zip")
        rain_cover = request.POST.get("rain_cover")
        ladder = request.POST.get("ladder")
        straps = request.POST.get("straps")

        TentCheck.objects.get_or_create(rod=rod, mattress=mattress, zip=zip,
                                        rain_cover=rain_cover, ladder=ladder, straps=straps,
                                        user=user)

        return redirect("app:create_status", pk=user.pk)

    else:
        return render(request, "tent/tent_create_check.html")


def tent_update_check(request, pk):
    tent = TentCheck.objects.get(pk=pk)
    if request.method == "POST":
        users = User.objects.get(pk=tent.user.pk)
        rod = request.POST.get("rod")
        mattress = request.POST.get("mattress")
        zip = request.POST.get("zip")
        rain_cover = request.POST.get("rain_cover")
        ladder = request.POST.get("ladder")
        straps = request.POST.get("straps")

        TentCheck.objects.update(rod=rod, mattress=mattress, zip=zip,
                                 rain_cover=rain_cover, ladder=ladder, straps=straps,
                                 user=users)

        return redirect("app:show_status", pk=users.pk)

    else:
        return render(request, "tent/tent_update_check.html", {"tent": tent})
