from django.shortcuts import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *


class PostView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk, user=request.user)
        serializer = PostSerializer(post)
        return Response(serializer.data)
    
    def post(self,request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    
    
class PostListView(APIView):
    
    def get(self, request):
        post = Post.objects.filter(is_active=True)
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)
    
    
class PostFileListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, post):
        files = PostFile.objects.filter(post=post)
        serializer = PostFileSerializer(files, many=True)
        return Response(serializer.data)
    
    def post(self, request, post):
        serializer = PostFileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(post=post)
        return Response(status=status.HTTP_201_CREATED)
            

class PostFileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, post, pk):
        file = get_object_or_404(PostFile, pk=pk, post=post)
        serializer = PostFileSerializer(file)
        return Response(serializer.data)
    
    
class CommentView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, post):
        post = get_object_or_404(Post, pk=post)
        comment = post.comments.filter(is_approved=True)
        serializer = CommentSerializer(comment, many=True)
        return Response(serializer.data)  
    
    def post(self, request, post):
        get_object_or_404(Post, pk=post)
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, post=post)
        return Response(serializer.data)
    

class LikeView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, post):
        post = get_object_or_404(Post, pk=post)
        like = post.likes.filter(is_liked=True).count()
        serializer = LikeSerializer(like, many=True)
        return Response(serializer.data)  
    
    def post(self, request, post):
        get_object_or_404(Post, pk=post)
        serializer = LikeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, post=post)
        return Response(serializer.data)
        
        

        