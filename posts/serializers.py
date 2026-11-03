from rest_framework import serializers

from .models import *


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        fields = '__all__'
        extra_kwargs = {
            "user":{'read_only': True}
        }
        

class PostFileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PostFile
        fields = '__all__'
        
        
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True},
                        'post': {'read_only': True}}
        
        
class LikeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Like
        fields = '__all__'
        extra_kwargs = {'user': {'read_only': True},
                        'post': {'read_only': True},
                        'is_liked': {'required': False}}
        