from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField("Аватарка", null=True, blank=True, upload_to='avatar/')
    fullname = models.CharField("Полное имя", max_length=50, null=True, blank=True)
    location = models.CharField("Местоположение", max_length=100, null=True, blank=True)
    about = models.TextField("О себе", max_length=255, null=True, blank=True)
    website = models.CharField("Веб-сайт", max_length=100, null=True, blank=True)

    def __str__(self):
        return f"{self.fullname} (@{self.user.username})"
