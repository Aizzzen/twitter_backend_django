from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from tweet.models import Tweet
from tweet.permissions import IsOwnerOrReadOnly
from tweet.serializers import TweetSerializer


class TweetAPIList(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class TweetAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (IsOwnerOrReadOnly, )
