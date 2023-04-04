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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from backend import settings
from tweet.views import TweetAPIList, TweetAPIUpdateDestroy
from user.views import ActivationView     # get_all_user_data

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),

    path('api/v1/activate/<uidb64>/<token>/', ActivationView.as_view(), name='activate'),

    # path('api/v1/user/', get_all_user_data, name='user'),

    path('api/v1/tweets/', TweetAPIList.as_view()),
    path('api/v1/tweets/<int:pk>/', TweetAPIList.as_view()),
    path('api/v1/tweets/<int:pk>/', TweetAPIUpdateDestroy.as_view()),
]

# При дебаге добавляем маршрут для статических файлов
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
