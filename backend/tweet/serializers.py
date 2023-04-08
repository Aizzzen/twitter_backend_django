from rest_framework import serializers

from tweet.models import Tweet


class TweetSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username')
    # first_name = serializers.CharField(source='user.first_name')
    # last_name = serializers.CharField(source='user.last_name')
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Tweet
        fields = "__all__"
