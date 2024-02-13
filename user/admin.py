from django.contrib.admin import ModelAdmin, register
from .models import CustomUser, PaymentDate, Subscription

@register(CustomUser)
class UserAdmin(ModelAdmin):
    list_display = ('username', 'email')
    
@register(Subscription)
class SubscriptionAdmin(ModelAdmin):
    list_display = ("subscription_name", "price", "valid_time")    

@register(PaymentDate)
class PaymentAdmin(ModelAdmin):
    list_display = ("user", "payment_date", "valid_date")