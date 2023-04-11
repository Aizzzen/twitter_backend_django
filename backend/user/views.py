from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.views import View
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view

from tweet.models import Tweet, Media
from .serializers import UserSerializer


@api_view(['GET'])
def get_user_data(request: Request):
    return Response({
        **UserSerializer(request.user).data,
    })


class ActivationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if user.is_active:
                return render(request, 'user/base.html', {'title': 'Ваша учетная запись уже активирована'})
            user.is_active = True
            user.save()

            return render(request, 'user/base.html', {'title': 'Ваша учетная запись была успешно активирована'})

        except Exception as ex:
            HttpResponse('Something went wrong')

        return render(request, 'user/base.html', {'title': 'Ваша учетная запись была успешно активирована'})
