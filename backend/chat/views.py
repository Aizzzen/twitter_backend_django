from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from chat.models import Chat, Message
from chat.serializers import ShowChatsSerializer, NewChatSerializer, ListMessageSerializer, GetUserDataForChat
from chat.pagination import MessagesPagination
from user.models import Profile


def index(request):
    return render(request, "index.html")


def room(request, room_name):
    return render(request, "room.html", {"room_name": room_name})


class NewChatView(APIView):
    queryset = Chat.objects.all()
    serializer_class = NewChatSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = NewChatSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            chat = serializer.save()
            data['chat_id'] = chat.id
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class ChatsShowView(APIView):
    serializer_class = ShowChatsSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = ShowChatsSerializer(request)
        chats = serializer.list(request)
        return Response({'data': chats})


class ListMessageView(APIView):
    queryset = Message.objects.all()
    serializer_class = ListMessageSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        chat = Chat.objects.get(pk=pk)
        queryset = Message.objects.filter(chat=chat).order_by('-id')
        paginator = MessagesPagination()
        page = paginator.paginate_queryset(queryset, request)
        serializer = ListMessageSerializer(page, many=True)
        user = chat.users.all().exclude(id=request.user.id).values('id', 'username')[0],
        profile = chat.users.all().exclude(id=request.user.id).values('profile')[0],
        if profile:
            fullname = Profile.objects.filter(id=profile[0]['profile']).values('fullname')[0]['fullname']
            return_user = user[0]
            return_user['fullname'] = fullname
            data = {
                'msgs': paginator.get_paginated(serializer.data),
                'user': return_user,
            }
            return Response(data)
        else:
            return_user = user[0]
            data = {
                'msgs': paginator.get_paginated(serializer.data),
                'user': return_user,
            }
            return Response(data)


class GetUserData(RetrieveAPIView):
    # queryset = User.objects.all()
    serializer_class = GetUserDataForChat
    permission_classes = [IsAuthenticated]

    def get(self, request):
        queryset = User.objects.get(id=request.user.id)
        serializer = GetUserDataForChat(queryset)
        return Response(serializer.data)
