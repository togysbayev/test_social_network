from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:id>/', views.PostDetail.as_view())
]