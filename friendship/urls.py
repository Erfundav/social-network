from django.urls import path

from .views import *


urlpatterns = [
    path('user-list/', UserListView.as_view()),
    path('request/', RequestView.as_view()),
    path('request-list/', RequestListView.as_view()),
    path('accept/', AcceptView.as_view()),
    path('friends-list/', FriendListView.as_view()),
]