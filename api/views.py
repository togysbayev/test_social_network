from django.shortcuts import render, get_object_or_404
from rest_framework import status, generics
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Post
from .serializers import PostSerializer, PostLikeSerializer
from .permissions import IsOwnerOfPost
from rest_framework.mixins import UpdateModelMixin
from rest_framework.viewsets import ModelViewSet


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['head', 'options', 'get', 'post', 'put']
    
    # def get_serializer_class(self):
    #     if self.action == 'like':
    #         return None
    #     return PostSerializer
    
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        elif self.request.method in ['PUT', 'DELETE']:
            return [IsOwnerOfPost()]
        elif self.action in ['like', 'dislike']:
            return [IsAuthenticated()]
        return [AllowAny()]
    
    
    @action(detail=True)
    def like(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.likes.add(request.user)
        post.save()
        return Response("You liked the post!")
    
    @action(detail=True)
    def dislike(self, request, pk):
        post = Post.objects.get(pk=pk)
        post.dislikes.add(request.user)
        post.save()
        return Response("You disliked the post!")
        


# class PostList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     http_method_names = ['head', 'options', 'get', 'post']
    
#     def get_permissions(self):
#         if self.request.method == 'POST':
#             return [IsAuthenticated()]
#         return [AllowAny()]
    
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     http_method_names = ['head', 'options', 'get', 'put', 'delete']

#     def get_permissions(self):
#         if self.request.method in ['PUT', 'DELETE']:
#             return [IsOwnerOfPost()]
#         return [AllowAny()]
    
#     @action(detail=True)
#     def like(self, request):
#         return Response('ok')
    
# @api_view(['POST'])
# def like_post(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     if request.method == 'POST':
#         post.likes.add(request.user)
#         post.save()
#         return Response("You liked the post", status=status.HTTP_201_CREATED)

    
    
    
    
    
    
    
# class PostLike(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = LikeSerializer
    
#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"message": "You liked the post"})

#         else:
#             return Response({"message": "failed", "details": serializer.errors})
