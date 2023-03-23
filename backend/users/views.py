from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import UserSerializer, UserProfileSerializer


@api_view()
def user(request: Request):
    return Response({
        'user_data': UserSerializer(request.user).data,
        'user_profile_data': UserProfileSerializer(request.user).data
    })


# UserProfileSerializer(request.user).data
