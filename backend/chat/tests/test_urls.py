from django.test import SimpleTestCase
from django.urls import resolve, reverse
from chat.views import (
    NewChatView,
    ChatsShowView,
    ListMessageView,
    GetUserData
)


class TestUrls(SimpleTestCase):
    def setUp(self):
        self.chat_new_url = reverse('new')
        self.chat_view_url = reverse('view')
        self.chat_listmsgs_url = reverse('listmsgs', args=[1])
        self.chat_user_url = reverse('user')

    def test_chat_new_url_is_resolved(self):
        url = self.chat_new_url
        self.assertEqual(resolve(url).func.view_class, NewChatView)

    def test_chat_view_url_is_resolved(self):
        url = self.chat_view_url
        self.assertEqual(resolve(url).func.view_class, ChatsShowView)

    def test_chat_listmsgs_url_is_resolved(self):
        url = self.chat_listmsgs_url
        self.assertEqual(resolve(url).func.view_class, ListMessageView)

    def test_chat_user_url_is_resolved(self):
        url = self.chat_user_url
        self.assertEqual(resolve(url).func.view_class, GetUserData)
