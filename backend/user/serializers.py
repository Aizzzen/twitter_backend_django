from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'is_active', 'date_joined', )


# class UserProfileSerializer(ModelSerializer):
#     class Meta:
#         model = UserProfile
#         fields = ('fullname', 'location', 'about', 'website',
#                   'tweet',
#         )
#
