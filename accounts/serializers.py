from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator


User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True, 
        validators=[UniqueValidator(queryset=User.objects.all())]
        )
    password_1 = serializers.CharField(required=True, write_only=True)
    password_2 = serializers.CharField(required=True, write_only=True)
    
    class Meta:
        model = User
        fields = ('email', 'username', 'password_1', 'password_2', 'first_name', 'last_name')
        extra_kwargs = {'first_name': {'required': False},
                        'last_name': {'required': False}}
        
    def validate(self, attrs):
        if attrs['password_1'] != attrs['password_2']:
            raise serializers.ValidationError({
                'password': 'Password did not match'
            })
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password_2')
        password = validated_data.pop('password_1')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user
    
    
class UserSerializer(serializers.ModelSerializer):
    avatar = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['id', 'username', 'avatar']
        
    def get_avatar(self, instance):
        if hasattr(instance, 'profile') and instance.profile.avatar:
            return instance.profile.avatar.url
        return ''