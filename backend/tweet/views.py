from urllib.request import Request

from requests import Response
from rest_framework import generics
from rest_framework.decorators import api_view, action
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from tweet.models import Tweet
from tweet.permissions import IsOwnerOrReadOnly
from tweet.serializers import TweetSerializer


class TweetAPIList(generics.ListCreateAPIView):
    # queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Tweet.objects.all()

        return Tweet.objects.filter(pk=pk)


class TweetAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (IsOwnerOrReadOnly, )
