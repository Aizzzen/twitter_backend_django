from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from chat.models import Chat, Message
from user.models import Profile


class TestViews(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='yunus111@gmail.com',
            username='yunus111',
            password='yunus111',
        )
        profile = Profile.objects.create(user=self.user, fullname='Yunus Gadamurov')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.chat_new_url = reverse('new')
        self.chat_view_url = reverse('view')
        self.chat_listmsgs_url = reverse('listmsgs', args=[1])
        self.chat_user_url = reverse('user')

    def test_chat_new_url_POST(self):
        user1 = User.objects.create_user(
            email='yunus222@gmail.com',
            username='yunus222',
            password='yunus222',
        )
        user2 = User.objects.create_user(
            email='yunus333@gmail.com',
            username='yunus333',
            password='yunus333',
        )
        response = self.client.post(self.chat_new_url, {
            'user1': user1,
            'user2': user2,
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_chat_view_url_GET(self):
        response = self.client.get(self.chat_view_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_chat_listmsgs_url_GET(self):
    #     Chat.objects.create()
    #     response = self.client.get(self.chat_listmsgs_url)
    #     self.assertEqual(response.status_code, 200)

    # def test_chat_user_url_GET(self):
    #     response = self.client.get(self.chat_user_url)
    #     self.assertEqual(response.status_code, 200)
