from django.urls import path
from .views import HomeView

urlpatterns = [
    path('', HomeView.as_view()),
    # path('create/', post_create),
    # path('<post_id>/', post_detail),
    # path('edit/<post_id>', post_update),
    # path('delete/<post_id>', post_delete),
]
