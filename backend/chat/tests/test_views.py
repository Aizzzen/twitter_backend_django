from django.test import TestCase, Client
from django.urls import reverse
from chat.models import Chat, Message
from chat.views import (
    NewChatView,
    ChatsShowView,
    ListMessageView,
    GetUserData
)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.chat_new_url = reverse('new')
        self.chat_view_url = reverse('view')
        self.chat_listmsgs_url = reverse('listmsgs', args=[1])
        self.chat_user_url = reverse('user')

    def test_chat_new_url_POST(self):
        response = self.client.post(self.chat_new_url)
        self.assertEqual(response.status_code, 401)

    def test_chat_view_url_GET(self):
        response = self.client.get(self.chat_view_url)
        self.assertEqual(response.status_code, 401)

    def test_chat_listmsgs_url_GET(self):
        response = self.client.get(self.chat_listmsgs_url)
        self.assertEqual(response.status_code, 401)

    def test_chat_user_url_GET(self):
        response = self.client.get(self.chat_user_url)
        self.assertEqual(response.status_code, 401)
