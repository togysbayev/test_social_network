from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework import generics 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerOfPost


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['head', 'options', 'get', 'post']
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        return [AllowAny()]
    
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['head', 'options', 'get', 'put', 'delete']

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [IsOwnerOfPost()]
        return [AllowAny()]