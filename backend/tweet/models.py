from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.db import models


class Tweet(models.Model):
    text = models.TextField(validators=[MaxLengthValidator(280)])
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # likes = models.PositiveIntegerField(null=True, default=0)
    # retweets
    # replies

    class Meta:
        ordering = ['-is_created', ]
