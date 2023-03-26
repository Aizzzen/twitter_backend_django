from django.contrib.auth.models import User
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from tweet.models import Tweet
from .serializers import UserSerializer, UserProfileSerializer


@api_view(['GET'])
def get_all_user_data(request: Request):
    return Response({
        # 'data': {
        **UserSerializer(request.user).data,
        **UserProfileSerializer(request.user).data,
        # 'tweets': Tweet.objects.all().values()  # - если не авторизован
        'tweets': Tweet.objects.filter(user=request.user).values()  # - если авторизован
        # },
    })

# @api_view(['GET'])
# def get_all_users(request: Request):
#     return Response({
#         'users': User.objects.all().values()
#     })
