from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    verified = models.BooleanField(default = False)
    
    
    def __str__(self):
        return self.username
    
    
class Subscription(models.Model):
    subscription_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField()
    valid_time = models.PositiveIntegerField()
    
    def __str__(self):
        return self.subscription_name
    

class PaymentDate(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    subscription = models.ForeignKey(Subscription, on_delete=models.CASCADE, null = True, blank = True)
    payment_date = models.DateField()
    valid_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Subscription of {self.user.username} is valid till {self.valid_date}"
    
    
        