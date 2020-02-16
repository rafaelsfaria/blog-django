from django.urls import path
from .views import HomeView, PostView, PostCreate

urlpatterns = [
    path('', HomeView.as_view(),name='home'),
    path('posts/create/', PostCreate.as_view(success_url='/'), name='post-create'),
    path('posts/<int:pk>/', PostView.as_view(), name='post-detail'),
    # path('edit/<post_id>', post_update),
    # path('delete/<post_id>', post_delete),
]
