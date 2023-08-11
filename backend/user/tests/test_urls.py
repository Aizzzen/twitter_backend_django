from django.test import TestCase
from django.urls import resolve, reverse
from user.views import (
    UserAPIView,
    ActivationView
)


class TestUrls(TestCase):
    def setUp(self):
        self.activate_url = reverse('activate', args=['MNQ', 609355393763470])
        self.userdata_url = reverse('userdata')

    def test_activate_url_is_resolved(self):
        url = self.activate_url
        self.assertEqual(resolve(url).func.view_class, ActivationView)

    def test_userdata_url_is_resolved(self):
        url = self.userdata_url
        self.assertEqual(resolve(url).func.view_class, UserAPIView)
