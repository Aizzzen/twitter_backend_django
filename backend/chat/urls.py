from django.urls import path
from .views import NewChatView, ChatsShowView, ListMessageView, GetUserData
# from .views import index, room


urlpatterns = [
    # path('chat/', index, name='index'),
    # path("chat/<str:room_name>/", room, name='room'),
    path('chat/new/', NewChatView.as_view(), name='new'),
    path('chat/view/', ChatsShowView.as_view(), name='view'),
    path('chat/listmsgs/<int:pk>/', ListMessageView.as_view(), name='listmsgs'),
    path('chat/user/', GetUserData.as_view(), name='user'),
]
