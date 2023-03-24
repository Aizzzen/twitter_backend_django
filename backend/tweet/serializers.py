from rest_framework import serializers

from tweet.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Tweet
        fields = "__all__"
