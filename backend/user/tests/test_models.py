from django.contrib.auth.models import User
from django.test import TestCase
from user.models import Profile


class TestModels(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email='yunus111@gmail.com',
            username='yunus111',
            password='yunus111',
        )

    def test_user_can_be_created(self):
        self.assertEqual(self.user.email, 'yunus111@gmail.com')
        self.assertEqual(self.user.username, 'yunus111')
        self.assertTrue(self.user.is_active)

    def test_user_profile_can_be_created(self):
        profile = Profile.objects.create(user=self.user, fullname='Yunus Gadamurov')
        self.assertEqual(profile.fullname, 'Yunus Gadamurov')
