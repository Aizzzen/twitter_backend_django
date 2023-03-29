from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.db import models


class Tweet(models.Model):
    text = models.TextField(validators=[MaxLengthValidator(280)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # likes = models.PositiveIntegerField(null=True, default=0)
    # retweets
    # replies

    class Meta:
        ordering = ['-created_at', ]
