from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.db.models import Q
from django.contrib.auth.hashers import make_password
from .models import CustomUser, PaymentDate, Subscription
from django.contrib.auth.decorators import login_required
import requests as req
import uuid
from datetime import datetime
from dateutil.relativedelta import relativedelta


@login_required
def logoutUser(request):
    logout(request)
    return redirect("login")

def loginUser(request):
    if request.user.is_authenticated:
        return redirect("home")
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
                    login(request, user)
                    messages.success(request, "Logged in successfully")
                    return redirect("home")
                else:
                    login(request, user)
                    messages.warning(request, "Please select the subscription to watch movies")
                    return redirect("subscription")
            else:
                messages.warning(request, "User doesn't exist")
                return redirect("login")
    return render(request, "login.html")



def registerUser(request):
    if request.user.is_authenticated:
        return redirect("home")
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
                login(request,user)
                messages.success(request, "User successfuly registered")
                return redirect("subscription")
    return render(request, "register.html")


def subscriptionView(request):
    if request.user.verified:
        return redirect("home")
    pid = uuid.uuid4()
    subscriptions = Subscription.objects.all()
    return render(request, "subscriptionPage.html", {"subscriptions": subscriptions, "pid": pid})

def payment_response(request):
    url ="https://uat.esewa.com.np/epay/transrec"
    d = {
        'amt': request.GET.get("amt"),
        'scd': 'EPAYTEST',
        'rid': '000AE01',
        'pid':request.GET.get("pid"),
    }
    resp = req.post(url, d)
    amt = d['amt'].split(".")
    if resp.status_code == 200:
        subs = Subscription.objects.filter(price = int(amt[0])).first()
        valid_date  = datetime.now().date() + relativedelta(months = 3)
        payment_date = datetime.now().date()
        payment = PaymentDate.objects.create(user = request.user, subscription=subs, payment_date= payment_date, valid_date=valid_date)
        payment.save()
        user = request.user
        user.verified = True
        user.save()
        messages.success(request, "Subscription successfully added")
        return redirect("home")
    else:
        messages.warning(request, "Payment not verified")
        return redirect("subscription")
    return redirect("login")