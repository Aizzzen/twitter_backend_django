"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from user.views import user
from tweet.views import *
from rest_framework import routers


router = routers.SimpleRouter()
router.register(r'tweet', TweetViewSet, basename='tweet')

urlpatterns = [
    path('admin/', admin.site.urls),

    # path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.jwt')),
    # path('auth/user/', user, name='user'),
    # path('api/v1/', include(router.urls)),


    # path('api/v1/tweet/', TweetAPIList.as_view()),
    # path('api/v1/tweet/<int:pk>/', TweetAPIUpdate.as_view()),
    # path('api/v1/tweetdetail/<int:pk>/', TweetDetailAPI.as_view()),

    path('api/v1/', include(router.urls)),

]

urlpatterns += router.urls
