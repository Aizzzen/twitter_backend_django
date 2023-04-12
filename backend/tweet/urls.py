from django.urls import path
from .views import TweetAPIListCreate, TweetAPIUpdateDestroy, get_user_tweets

urlpatterns = [
    path('tweets/', TweetAPIListCreate.as_view()),
    path('tweets/<int:pk>/', TweetAPIListCreate.as_view()),
    path('tweets-detail/<int:pk>/', TweetAPIUpdateDestroy.as_view()),
    path('tweets-data/', get_user_tweets),
]
