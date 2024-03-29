from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from django.db import models
from user.serializers import UserSerializer, ProfileSerializer
from user.models import Profile


class Tweet(models.Model):
    text = models.TextField("Текст твита", validators=[MaxLengthValidator(280)])
    created_at = models.DateTimeField("Время создания", auto_now_add=True)
    updated_at = models.DateTimeField("Время обновления", auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField("Лайки", null=True, default=0)

    def get_username(self):
        return self.user

    def get_fullname(self):
        user = Profile.objects.get(user=self.user.pk)
        serializer = ProfileSerializer(user)
        fullname = serializer.data['fullname']
        if fullname:
            return fullname
        else:
            return None

    class Meta:
        ordering = ['-created_at', ]


class Media(models.Model):
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="photos")
    media = models.ImageField("Медиа твита", null=True, blank=True, upload_to='photos/%Y/%m/%d/')


class Comment(models.Model):
    text = models.TextField("Комментарий", validators=[MaxLengthValidator(280)])
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField("Время создания", auto_now_add=True)

    def get_username(self):
        return self.user

    def get_fullname(self):
        user = Profile.objects.get(user=self.user.pk)
        serializer = ProfileSerializer(user)
        fullname = serializer.data['fullname']
        if fullname:
            return fullname
        else:
            return None
