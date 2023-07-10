from django.urls import path, include

from user.views import ActivationView, UserAPIView

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('activate/<uidb64>/<token>/', ActivationView.as_view(), name='activate'),
    path('user-data/', UserAPIView.as_view()),
    # path('user-data/', get_user_data),
]
