from django.urls import path
from . import views


urlpatterns = [
    path("", views.loginUser,name = "login"),
    path("register/", views.registerUser, name = "register"),
    path("subscription/", views.subscriptionView, name = "subscription"),
    path("logout/", views.logoutUser, name = "logout"),
    path("verify_payment/", views.payment_response, name = "verify-payment")
]
