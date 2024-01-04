from . import views
from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', views.apiOverview, name="api-overview"),
    path('blog-list-create/', views.postlist, name="blog-list"),
    path('blog-get-update-delete/<str:pk>/', views.postdetail, name='blog-detail'),
    path('blog-comments/', views.get_comments, name='comments'),
    path('blog-comments-create/', views.create_comment, name='create-comments'),
    path('blog-comments-update/<str:pk>/', views.update_comment, name='update-comments'),
    path('blog-comments-delete/<str:pk>/', views.delete_comment, name='delete-comments'),
]