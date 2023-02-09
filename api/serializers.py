from django.contrib.auth.models import User
from djoser.serializers import UserSerializer as BaseUserSerializer, UserCreateSerializer as BaseUserCreateSerializer
from .models import Post
from rest_framework import serializers

class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ['id', 'username', 'email', 'first_name', 'last_name']
        
class UserCreateSerializer(BaseUserCreateSerializer):
    class Meta(BaseUserCreateSerializer.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

class PostSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'body', 'likes', 'created_at', 'updated_at']
