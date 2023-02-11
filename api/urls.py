from django.urls import path
from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet)

urlpatterns = router.urls

# urlpatterns = [
#     path('posts/', views.PostList.as_view()),
#     path('posts/<int:pk>/', views.PostDetail.as_view()),
#     path('posts/<int:pk>/like/', views.like_post)
# ]