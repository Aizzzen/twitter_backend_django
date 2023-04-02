from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.models import User
from django.views import View
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


class ActivationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            # if user.is_active:
            #     return redirect('login')
            user.is_active = True
            user.save()

            # messages.success(request, 'Account activated successfully')
            # return redirect('login')
            return HttpResponse('Активация прошла успешно')

        except Exception as ex:
            pass

        # return redirect('login')
        return HttpResponse('Активация прошла успешно')
