from django.db import models
from .user import User

class OfficeUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, null=True, blank=True, default='')
    profession = models.CharField(max_length=75, null=True, blank=True, default='')
    aboutMe = models.TextField(max_length=3000, null=True, blank=True, default='')
    profileImage = models.ImageField(null=True, blank=True, upload_to="userImages/")
    isAdmin = models.BooleanField(default=False)
