from django.contrib.auth.models import User

from django.db import models


class Chat(models.Model):
    users = models.ManyToManyField(User)


class Message(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    text = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now=True)
    chat = models.ForeignKey(Chat, null=True, on_delete=models.SET_NULL)
