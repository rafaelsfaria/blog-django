from django.urls import path
from .views import post_list, post_detail, post_create, post_update, post_delete

urlpatterns = [
  path('', post_list),
  path('create/', post_create),
  path('<post_id>/', post_detail),
  path('edit/<post_id>', post_update),
  path('delete/<post_id>', post_delete),
]