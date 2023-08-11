from django.contrib.auth.models import User
from django.test import TestCase
from user.models import Profile
from tweet.models import Tweet


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='yunus111@gmail.com',
            username='yunus111',
            password='yunus111',
        )
        profile = Profile.objects.create(user=self.user, fullname='Yunus Gadamurov')

    def test_tweet_can_be_created(self):
        tweet = Tweet.objects.create(
            user=self.user,
            text='Test tweet'
        )
        self.assertEqual(tweet.text, 'Test tweet')
        self.assertEqual(tweet.user, self.user)
        self.assertEqual(tweet.likes, 0)

    # def test_tweet_profile_can_be_created(self):
    #     profile = Profile.objects.create(user=self.user, fullname='Yunus Gadamurov')
    #     self.assertEqual(profile.fullname, 'Yunus Gadamurov')
