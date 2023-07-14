from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth.models import User
from django.views import View
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Profile
from .serializers import UserSerializer, ProfileSerializer


class UserAPIView(APIView):
    def get(self, request):
        user = User.objects.get(username=request.user.username)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        instance = Profile.objects.get(user=request.user.id)
        if instance:
            # data - create / data + instance - update (in serializer)
            serializer = ProfileSerializer(data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"updated_profile": serializer.data})
        else:
            return Response({"message": "Метод PUT не разрешен"})


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
