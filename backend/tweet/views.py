from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response

from tweet.models import Tweet, Media
from tweet.permissions import IsOwnerOrReadOnly
from tweet.serializers import TweetSerializer
from user.serializers import UserSerializer


class TweetAPIList(generics.ListCreateAPIView):
    serializer_class = TweetSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Tweet.objects.all()

        return Tweet.objects.filter(pk=pk)

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        for tweet in serializer.data:
            # tweet['username'] = User.objects.all().values().get(pk=tweet['user'])['username']
            tweet['photos'] = Media.objects.filter(tweet=tweet['id']).values()
            # tweet['username'] = User.objects.all().values().get(pk=tweet['user'])
        return Response(serializer.data)

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
            'photos': Media.objects.filter(tweet=serializer.data['id']).values()
        }, status=status.HTTP_201_CREATED, headers=headers)


class TweetAPIUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer
    permission_classes = (IsOwnerOrReadOnly, )

