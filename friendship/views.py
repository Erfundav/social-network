from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .serializers import FriendshipSerializer
from accounts.serializers import UserSerializer
from .models import Friendship


User = get_user_model()

class UserListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        q = request.query_params.get('q')
        if q:
            users = User.objects.filter(usersname__icontains=q)
        else:
            users = User.objects.filter(is_superuser=False, is_staff=False)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    
class RequestView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user_id = request.data.get('user')  #in body: {"user": 1}
        user = get_object_or_404(User, pk=user_id)
        Friendship.objects.get_or_create(request_from=request.user, requset_to=user)
        return Response({'detail': 'Request sent'}, status=status.HTTP_201_CREATED)
        
        
class RequestListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        friendships = Friendship.objects.filter(requset_to=request.user, is_accepted=False)
        users = [f.request_from for f in friendships]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    
class AcceptView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        user_id = request.data.get('user')
        user = get_object_or_404(User, pk=user_id)
        friendship = get_object_or_404(Friendship, request_from=user, requset_to=request.user, is_accepted=False)
        
        if not friendship.as_accepted:
            friendship.is_accepted = True
            friendship.save()
            return Response({'detail': 'accepted'}, status=status.HTTP_202_ACCEPTED)
        return Response({'detai': 'already accepted'})
    
    
class FriendListView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        friendships = Friendship.objects.filter(
            Q(request_from=request.user) | Q(requset_to=request.user),
            is_accepted=True
        )
        print(friendships.query)
    
        users = [f.request_from for f in friendships]
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)