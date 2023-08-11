from django.contrib.auth.models import User
from django.test import TestCase
from user.models import Profile
from chat.models import Chat
from chat.models import Message


class TestModels(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(
            email='yunus111@gmail.com',
            username='yunus111',
            password='yunus111',
        )
        profile1 = Profile.objects.create(user=self.user1, fullname='Yunus G')
        self.user2 = User.objects.create_user(
            email='yunus222@gmail.com',
            username='yunus222',
            password='yunus222',
        )
        profile2 = Profile.objects.create(user=self.user2, fullname='Y Gadamurov')

    def test_chat_can_be_created(self):
        chat = Chat.objects.create()
        user1_id = self.user1.id
        user2_id = self.user2.id
        chat.users.set([user1_id, user2_id])
        message = Message.objects.create(
            chat=chat,
            user=self.user1,
            text='Test message'
        )
        self.assertEqual(message.user, self.user1)
        self.assertEqual(message.text, 'Test message')
        self.assertEqual(message.chat, chat)
