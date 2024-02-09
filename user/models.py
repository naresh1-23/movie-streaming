from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    verified = models.BooleanField(default = False)
    
    
    def __str__(self):
        return self.username
    
    

class PaymentDate(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    payment_date = models.DateField()
    valid_date = models.DateField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Subscription of {self.user.username} is valid till {self.valid_date}"
    
    
        