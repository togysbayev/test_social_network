from django.contrib.auth.models import User
from .models import Post
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class PostSerializer(serializers.ModelSerializer):
    # author_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author_id', 'title', 'body', 'likes', 'created_at', 'updated_at']
