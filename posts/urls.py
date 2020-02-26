from django.urls import path
from .views import (
    PostListView,
    PostUpdateView,
    PostDetailView,
    PostCreateView,
    CategoryDetailView,
    PostDeleteView,
    UserPostsView
)

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('users/<str:username>', UserPostsView.as_view(), name='user-posts'),
    path('posts/create/', PostCreateView.as_view(), name='post-create'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('posts/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('posts/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('categories/<str:slug>/', CategoryDetailView.as_view(), name='category-detail'),
]
