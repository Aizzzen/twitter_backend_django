from rest_framework.viewsets import ModelViewSet

from tweet.models import Tweet
from tweet.serializers import TweetSerializer


class TweetViewSet(ModelViewSet):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


# class TweetAPIList(generics.ListCreateAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#
#
# class TweetAPIUpdate(generics.UpdateAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
#
#
# class TweetDetailAPI(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Tweet.objects.all()
#     serializer_class = TweetSerializer
