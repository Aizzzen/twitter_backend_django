from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from chat.models import Chat, Message


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
            chats_res[chat_id] = {
                'user_id': chat_data_user.get().id,
                'username': chat_data_user.get().username,
            }
        return chats_res


# class SendMessageSerializers(serializers.ModelSerializer):
#     id_chat = serializers.IntegerField(write_only=True)
#     id_user = serializers.IntegerField(write_only=True)
#
#     class Meta:
#         model = Message
#         fields = ["id_chat", 'id_user', "text"]
#
#     def create(self, validated_data):
#         id_chat = validated_data.get('id_chat')
#         id_user = validated_data.get('id_user')
#         user = User.objects.get(id=id_user)
#         chat = Chat.objects.get(id=id_chat)
#         text = validated_data.get('text')
#         return Message.objects.create(user=user, chat=chat, text=text)


# class UserNameSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = '__all__'


# class ListMessageSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Message
#         fields = ['text', 'user']


# class GetUserDataForChat(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id', 'username']
