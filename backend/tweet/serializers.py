from rest_framework import serializers
from tweet.models import Tweet, Comment, Media


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='username', read_only=True)
    fullname = serializers.CharField(source='get_fullname', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'fullname', 'user', 'text', 'created_at', )


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class MediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Media
        fields = ('media', )


class TweetSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    comments = CommentSerializer(many=True, required=False)
    photos = MediaSerializer(many=True, required=False)
    username = serializers.CharField(source='get_username', read_only=True)
    fullname = serializers.CharField(source='get_fullname', read_only=True)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance

    class Meta:
        model = Tweet
        fields = ('id', 'username', 'fullname', 'text', 'photos', 'comments', 'likes', 'created_at', 'updated_at', 'user', )
