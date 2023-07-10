from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import UserSerializerDAB


class UserAPIView(APIView):
    def get(self, request):
        user = User.objects.get(username=request.user.username)
        serializer = UserSerializerDAB(user)
        return Response(serializer.data)


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
