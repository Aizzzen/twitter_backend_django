from django.urls import path
from .views import (
    TweetAPIListCreate,
    TweetAPIUpdateDestroy,
    CurrentUserTweets,
    CommentAPIView,
    CommentDetailAPIView
)

urlpatterns = [
    path('tweets/', TweetAPIListCreate.as_view()),
    path('tweets/<int:pk>/', TweetAPIListCreate.as_view()),
    path('tweets/detail/<int:pk>/', TweetAPIUpdateDestroy.as_view()),
    path('tweets/my/', CurrentUserTweets.as_view()),
    path('comments/', CommentAPIView.as_view()),
    path('comments/detail/<int:pk>/', CommentDetailAPIView.as_view()),
]
