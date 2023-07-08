from rest_framework import serializers

from tweet.models import Tweet, Comment, Media


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field="username", read_only=True)

    class Meta:
        model = Comment
        fields = ("user", "text", "created_at", )


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ("media", )


class TweetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    comments = CommentSerializer(many=True, required=False)
    photos = MediaSerializer(many=True, required=False)
    username = serializers.CharField(source='get_username', read_only=True)

    class Meta:
        model = Tweet
        # fields = "__all__"
        fields = ('id', 'username', 'text', 'photos', 'comments', 'likes', 'created_at', 'updated_at', 'user', )
