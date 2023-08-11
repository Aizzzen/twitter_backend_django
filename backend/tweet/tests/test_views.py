from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from tweet.models import Tweet
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
        self.list_tweets_url = reverse('listcreatetweets')
        self.list_one_url = reverse('listone', args=[1])
        self.detail_tweets_url = reverse('detailtweets', args=[3])

    def test_tweets_GET(self):
        response = self.client.get(self.list_tweets_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_one_tweet_url_GET(self):
        response = self.client.get(self.list_one_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_tweet_POST(self):
        response = self.client.post(self.list_tweets_url, {
            'text': 'first tweet'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_detail_tweets_url_PUT(self):
        Tweet.objects.create(
            text='setUpTextTweet',
            user=self.user
        )
        response = self.client.put(self.detail_tweets_url, {
            "text": "Updated Text"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_detail_tweets_url_DELETE(self):
        # Tweet.objects.create(
        #     text='setUpTextTweet',
        #     user=self.user
        # )
        # response = self.client.delete(self.detail_tweets_url)
        # self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
