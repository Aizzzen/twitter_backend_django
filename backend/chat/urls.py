from django.urls import path
from .views import index, room, NewChatView, ChatsShowView


urlpatterns = [
    # path('chat/', index, name='index'),
    # path("chat/<str:room_name>/", room, name='room'),

    path('chat/new/', NewChatView.as_view(), name='new'),
    path('chat/views/', ChatsShowView.as_view(), name='views'),
]
