from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from chat.models import Chat
from chat.serializers import ShowChatsSerializer, NewChatSerializer


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
