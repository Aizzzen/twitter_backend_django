from django.contrib.auth.models import User
from django.db.models import Prefetch
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.request import Request
from rest_framework.response import Response

from tweet.models import Tweet, Media, Comment
from tweet.permissions import IsOwnerOrReadOnly
from tweet.serializers import TweetSerializer


class TweetAPIListCreate(generics.ListCreateAPIView):
    serializer_class = TweetSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Tweet.objects.all()

        return Tweet.objects.filter(pk=pk)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        media = request.FILES.getlist('media')
        for photo in media:
            m = Media.objects.create(
                tweet=Tweet.objects.get(pk=serializer.data['id']),
                media=photo
            )

        return Response({
            **serializer.data,
            'photos': Media.objects.filter(tweet=serializer.data['id']).values(),
            'username': User.objects.all().values().get(tweet=serializer.data['id'])['username']
        }, status=status.HTTP_201_CREATED, headers=headers)
        # return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class TweetAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (IsOwnerOrReadOnly,)


@api_view(['GET'])
def get_user_tweets(request: Request):
    tweets = []
    for tweet in Tweet.objects.filter(user=request.user).values():
        tweet['photos'] = Media.objects.filter(tweet=tweet['id']).values()
        # tweet['comments'] = Comment.objects.filter(tweet=tweet['id']).values()
        tweet['username'] = User.objects.all().values().get(tweet=tweet['id'])['username']
        tweets.append(tweet)

    return Response(tweets)
