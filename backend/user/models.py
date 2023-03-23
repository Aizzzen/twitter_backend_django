from django.db import models
from django.contrib.auth.models import PermissionsMixin, User

from tweet.models import Tweet


# from django.contrib.auth.base_user import AbstractBaseUser
# from django.utils.translation import ugettext_lazy as _


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    location = models.CharField(max_length=255, null=True)
    fullname = models.CharField(max_length=255, null=True)
    about = models.CharField(max_length=255, null=True)
    website = models.CharField(max_length=255, null=True)
    # tweets = models.ForeignKey(Tweet, )
