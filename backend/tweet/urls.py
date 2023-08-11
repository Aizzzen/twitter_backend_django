from django.urls import path
from .views import (
    TweetAPIListCreate,
    TweetAPIUpdateDestroy,
    CurrentUserTweets,
    CommentAPIView,
    CommentDetailAPIView
)

urlpatterns = [
    path('tweets/', TweetAPIListCreate.as_view(), name='listcreatetweets'),
    path('tweets/<int:pk>/', TweetAPIListCreate.as_view(), name='listone'),
    path('tweets/detail/<int:pk>/', TweetAPIUpdateDestroy.as_view(), name='detailtweets'),
    path('tweets/my/', CurrentUserTweets.as_view(), name='mytweets'),
    path('comments/', CommentAPIView.as_view(), name='listcreatecomments'),
    path('comments/detail/<int:pk>/', CommentDetailAPIView.as_view(), name='detailcomments'),
]
