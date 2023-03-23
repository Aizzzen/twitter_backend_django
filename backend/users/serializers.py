from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

from users.models import UserProfile


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'is_active',)


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('fullname', 'location', 'about', 'website', 'tweets',)
