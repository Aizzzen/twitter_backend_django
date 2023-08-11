from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Profile


class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        # fields = ('avatar', 'fullname', 'location', 'about', 'website', )
        fields = ('fullname', 'location', 'about', 'website', )

    def update(self, instance, validated_data):
        # instance.avatar = validated_data.get('avatar', instance.avatar)
        instance.fullname = validated_data.get('fullname', instance.fullname)
        instance.location = validated_data.get('location', instance.location)
        instance.about = validated_data.get('about', instance.about)
        instance.website = validated_data.get('website', instance.website)
        instance.save()
        return instance


class UserSerializer(ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'is_active', 'date_joined', 'user', )
