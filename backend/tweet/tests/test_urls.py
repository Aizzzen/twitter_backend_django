from django.test import SimpleTestCase
from django.urls import resolve, reverse
from tweet.views import (
    TweetAPIListCreate,
    TweetAPIUpdateDestroy,
    CurrentUserTweets,
    CommentAPIView,
    CommentDetailAPIView
)


class TestUrls(SimpleTestCase):
    def setUp(self):
        self.list_tweets_url = reverse('listcreatetweets')
        self.list_one_tweet_url = reverse('listone', args=[1])
        self.detail_tweets_url = reverse('detailtweets', args=[1])
        self.my_tweets_url = reverse('mytweets')
        self.list_comments_url = reverse('listcreatecomments')
        self.detail_comments_url = reverse('detailcomments', args=[1])

    def test_listcreate_url_is_resolved(self):
        url = self.list_tweets_url
        self.assertEqual(resolve(url).func.view_class, TweetAPIListCreate)

    def test_list_url_is_resolved(self):
        url = self.list_one_tweet_url
        self.assertEqual(resolve(url).func.view_class, TweetAPIListCreate)

    def test_detailtweets_url_is_resolved(self):
        url = self.detail_tweets_url
        self.assertEqual(resolve(url).func.view_class, TweetAPIUpdateDestroy)

    def test_mytweets_url_is_resolved(self):
        url = self.my_tweets_url
        self.assertEqual(resolve(url).func.view_class, CurrentUserTweets)

    def test_listcreatecomments_url_is_resolved(self):
        url = self.list_comments_url
        self.assertEqual(resolve(url).func.view_class, CommentAPIView)

    def test_detailcomments_url_is_resolved(self):
        url = self.detail_comments_url
        self.assertEqual(resolve(url).func.view_class, CommentDetailAPIView)
