from rest_framework import serializers
from django.contrib.auth.models import User

from tweet.models import Tweet, Comment, Media


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = "__all__"


class TweetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    comments = CommentSerializer(many=True)
    photos = MediaSerializer(many=True)
    username = serializers.CharField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Tweet
        fields = ('id', 'text', 'username', 'photos', 'comments', 'created_at', 'updated_at', 'user', )
