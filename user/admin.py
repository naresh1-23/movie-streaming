from django.contrib.admin import ModelAdmin, register
from .models import CustomUser, PaymentDate

@register(CustomUser)
class UserAdmin(ModelAdmin):
    list_display = ('username', 'email')
    
@register(PaymentDate)
class PaymentAdmin(ModelAdmin):
    list_display = ("user", "payment_date", "valid_date")