from django.dispatch import receiver
from djoser.signals import user_registered

from user.models import Profile


@receiver(user_registered, dispatch_uid='create_profile')
def create_profile(sender, user, request, **kwargs):
    data = request.data

    Profile.objects.create(
        user=user,
        avatar=data.get('avatar'),
        fullname=data.get('fullname'),
        location=data.get('location'),
        about=data.get('about'),
        website=data.get('website'),
    )
