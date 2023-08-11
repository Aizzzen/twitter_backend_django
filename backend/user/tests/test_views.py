from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
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
        self.activate_url = reverse('activate', args=['MNQ', 10396941313464319070897])
        self.userdata_url = reverse('userdata')

    def test_activate_GET(self):
        response = self.client.get(self.activate_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTemplateUsed(response, 'user/base.html')

    # def test_userdata_url_GET(self):
    #     response = self.client.get(self.userdata_url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_userdata_url_non_authorized_PUT(self):
    #     response = self.client.put(self.userdata_url, {
    #         "fullname": 'Gadamurov Yu',
    #         "location": 'Russia',
    #         "about": '',
    #         "website": ''
    #     })
    #     self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
