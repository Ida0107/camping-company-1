from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from customer.models import Customer
from django.http import Http404

# Create your views here.


def signup(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")
        fname = request.POST.get("firstname")
        lname = request.POST.get("lastname")
        number = request.POST.get("number")

        if username == "" or password1 == "" or password2 == "" or email == "" or fname == "" or lname == "":
            raise Http404("All fields are mandatory")

        if password1 != password2:
            raise Http404("Both Passwords must match")

        user = User.objects.create_user(username=username, email=email,
                                        first_name=fname, last_name=lname)
        user.set_password(password1)

        user.save()

        Customer.objects.get_or_create(phone=number, user=user)
        login(request, user)
        return redirect("register:welcome")

    else:
        return render(request, "register/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_superuser:
                login(request, user)
                return redirect("app:represent")
            else:
                login(request, user)
                return redirect("customer:user_page")
        else:
            raise Http404("Password/Username is wrong")
    return render(request, "register/signin.html")


@login_required
def sign_out(request):
    logout(request)
    return redirect("app:home")


@login_required
def welcome(request):
    return render(request, "register/welcome.html")
