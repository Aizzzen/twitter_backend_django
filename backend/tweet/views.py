from django.contrib.auth.models import User
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from tweet.models import Tweet, Media, Comment
from tweet.permissions import IsOwnerOrReadOnly
from tweet.serializers import TweetSerializer, CommentSerializer, CommentCreateSerializer


class TweetAPIListCreate(generics.ListCreateAPIView):
    serializer_class = TweetSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        pk = self.kwargs.get('pk')

        if not pk:
            return Tweet.objects.all().select_related("user")

        return Tweet.objects.filter(pk=pk).select_related("user")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        self.check_object_permissions(request, serializer.data)
        headers = self.get_success_headers(serializer.data)

        media = request.FILES.getlist('media')
        for photo in media:
            m = Media.objects.create(
                tweet=Tweet.objects.get(pk=serializer.data['id']),
                media=photo
            )

        # return Response({
        #     **serializer.data,
        #     'photos': Media.objects.filter(tweet=serializer.data['id']).select_related("tweet").values(),
        #     'username': User.objects.all().values().get(tweet=serializer.data['id'])['username']
        # }, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class TweetAPIUpdateDestroy(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def put(self, request, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Tweet.objects.get(id=pk)
        self.check_object_permissions(request, instance)
        if instance:
            serializer = TweetSerializer(context={'request': request}, data=request.data, instance=instance)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"data": serializer.data})

    def delete(self, request, pk):
        tweet = Tweet.objects.get(pk=pk)
        self.check_object_permissions(request, tweet)
        tweet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CurrentUserTweets(APIView):
    def get(self, request):
        tweets = Tweet.objects.filter(user=request.user)
        serializer = TweetSerializer(tweets, many=True)
        return Response(serializer.data)


class CommentAPIView(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        comments = Comment.objects.all().select_related("tweet", "user")
        serializer = CommentSerializer(comments, many=True)
        self.check_object_permissions(request, comments)
        return Response(serializer.data)

    def post(self, request):
        serializer = CommentCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            self.check_object_permissions(request, serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentDetailAPIView(APIView):
    permission_classes = [IsOwnerOrReadOnly]

    def delete(self, request, pk):
        comment = Comment.objects.get(pk=pk)
        self.check_object_permissions(request, comment)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
