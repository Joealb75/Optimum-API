from django.db import models
from django.contrib.auth.models import User

class Consultation(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=15)
    status = models.CharField(max_length=50, default="New")
    assigned_to_user = models.ForeignKey(User, on_delete=models.CASCADE, default=4) #Change to Business Owners UserID
    created_date = models.DateField(auto_now_add=True)
    comment = models.TextField(max_length=1500)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
