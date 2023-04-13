from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class UserSerializerDAB(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'is_active', 'date_joined', )


# class ProfileSerializer(ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#
#     class Meta:
#         model = Profile
#         fields = ('id', 'user', 'fullname', 'location', 'about', 'website', )
#
