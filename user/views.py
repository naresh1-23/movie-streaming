from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from .models import CustomUser, PaymentDate
from django.contrib.auth.decorators import login_required

@login_required
def logoutUser(request):
    logout(request)
    return redirect("login")

def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        if username == "" or password == "":
            messages.warning(request, "Fields cannot be empty")
            return redirect("login")
        else:
            user = authenticate(username = username, password = password)
            if user:
                if user.verified:
                    messages.success(request, "Logged in successfully")
                    return redirect("home")
                else:
                    messages.warning(request, "Please select the subscription to watch movies")
                    return redirect("subscription")
            else:
                messages.warning(request, "User doesn't exist")
                return redirect("login")
    return render(request, "login.html")



def registerUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["confirm_password"]
        if password == "" or username == "" or email == "" or password2 == "":
            messages.warning(request, "Fields cannot be empty")
            return redirect("register")
        elif password != password2:
            messages.warning(request, "Password didn't matched")
            return redirect("register")
        else:
            user_check = CustomUser.objects.filter(Q(username = username) | Q(email = email)).first()
            if user_check:
                messages.warning(request, "Username or email already exist")
                return redirect("register")
            else:
                user = CustomUser.objects.create(username=username, email = email, password = make_password(password))
                user.save()
                messages.success(request, "User successfuly registered")
                return redirect("login")
    return render(request, "register.html")


def subscriptionView(request):
    return render(request, "subscriptionPage.html")