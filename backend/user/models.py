from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, null=True)
    fullname = models.CharField(max_length=255, null=True)
    about = models.CharField(max_length=255, null=True)
    website = models.CharField(max_length=255, null=True)
