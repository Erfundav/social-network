from django.urls import path

from .views import *


urlpatterns = [
    path('post/', PostView.as_view()),
    path('post/<int:pk>/', PostView.as_view()),
    path('posts/', PostListView.as_view()),
    path('post/<int:post>/files/', PostFileListView.as_view()),
    path('post/<int:post>/files/<int:pk>/', PostFileView.as_view()),
    path('post/<int:post>/comments/', CommentView.as_view()),
    path('post/<int:post>/likes/', LikeView.as_view()),
]