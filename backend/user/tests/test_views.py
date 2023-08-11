from django.test import TestCase, Client
from django.urls import reverse
from user.views import (
    UserAPIView,
    ActivationView
)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.activate_url = reverse('activate', args=['MNQ', 10396941313464319070897])
        self.userdata_url = reverse('userdata')

    def test_activate_GET(self):
        response = self.client.get(self.activate_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/base.html')

    def test_userdata_url_non_authorized_GET(self):
        response = self.client.get(self.userdata_url)
        self.assertEqual(response.status_code, 401)

    def test_userdata_url_non_authorized_PUT(self):
        response = self.client.put(self.userdata_url, {
            "fullname": 'Gadamurov Yu',
            "location": 'Russia',
            "about": '',
            "website": ''
        })
        self.assertEqual(response.status_code, 401)
