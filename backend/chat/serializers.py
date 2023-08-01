from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from chat.models import Chat, Message

from user.models import Profile


class NewChatSerializer(serializers.ModelSerializer):
    user1_id = serializers.IntegerField(write_only=True)
    user2_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Chat
        fields = ['user1_id', 'user2_id']

    def create(self, validated_data):
        user1_id = validated_data.get('user1_id')
        user2_id = validated_data.get('user2_id')
        try:
            chats = Chat.objects.filter(users=user1_id)
            chat = chats.get(users=user2_id)
        except ObjectDoesNotExist:
            instance = Chat.objects.create()
            instance.users.set([user1_id, user2_id])
            return instance
        else:
            return chat


class ShowChatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = "__all__"

    def list(self, request, *args, **kwargs):
        user_id = request.user.id
        chats_res = dict()
        chats = Chat.objects.filter(users__id=user_id).values_list('id', flat=True)
        for chat_id in chats:
            chat = Chat.objects.get(id=chat_id)
            chat_data_user = chat.users.exclude(id=user_id)
            profile = Profile.objects.filter(user_id=chat_data_user.get().id)
            if profile:
                fullname = profile.values('fullname')[0]['fullname']
                chats_res[chat_id] = {
                    'user_id': chat_data_user.get().id,
                    'username': chat_data_user.get().username,
                    'fullname': fullname
                }
            else:
                chats_res[chat_id] = {
                    'user_id': chat_data_user.get().id,
                    'username': chat_data_user.get().username,
                }
        return chats_res


class SendMessageSerializer(serializers.ModelSerializer):
    chat_id = serializers.IntegerField(write_only=True)
    user_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Message
        fields = ["chat_id", 'user_id', "text"]

    def create(self, validated_data):
        chat_id = validated_data.get('chat_id')
        user_id = validated_data.get('user_id')
        user = User.objects.get(id=user_id)
        chat = Chat.objects.get(id=chat_id)
        text = validated_data.get('text')
        return Message.objects.create(user=user, chat=chat, text=text)


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class ListMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['text', 'user', 'created_at']


class GetUserDataForChat(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']
