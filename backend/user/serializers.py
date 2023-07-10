from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = ('avatar', 'fullname', 'location', 'about', 'website', )


class UserSerializerDAB(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'is_active', 'date_joined', 'profile', )
