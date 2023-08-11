from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from tweet.models import Tweet, Media, Comment
from tweet.views import (
    TweetAPIListCreate,
    TweetAPIUpdateDestroy,
    CurrentUserTweets,
    CommentAPIView,
    CommentDetailAPIView
)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.list_tweets_url = reverse('listcreatetweets')
        self.list_one_url = reverse('listone', args=[1])
        self.detail_tweets_url = reverse('detailtweets', args=[1])

    def test_listcreate_GET(self):
        response = self.client.get(self.list_tweets_url)
        self.assertEqual(response.status_code, 200)

    def test_list_one_url_GET(self):
        response = self.client.get(self.list_one_url)
        self.assertEqual(response.status_code, 200)

    def test_listcreate_POST(self):
        response = self.client.post(self.list_tweets_url, {
            'text': 'first tweet'
        })
        self.assertEqual(response.status_code, 401)

    # def test_detail_tweets_url_PUT(self):
    #     response = self.client.put(self.detail_tweets_url, {
    #         "text": "Updated Text"
    #     })
    #     self.assertEquals(response.status_code, 401)
    #
    # def test_detail_tweets_url_DELETE(self):
    #     response = self.client.delete(self.detail_tweets_url)
    #     self.assertEquals(response.status_code, 401)
