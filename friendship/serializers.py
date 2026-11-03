from rest_framework.serializers import ModelSerializer

from .models import Friendship
from accounts.serializers import UserSerializer


class FriendshipSerializer(ModelSerializer):
    
    class Meta:
        model = Friendship
        fields = '__all__'
        