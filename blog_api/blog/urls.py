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
    path('post-list-create/', views.postlist, name="post-list"),
    path('post-get-update-delete/<str:pk>/', views.postdetail, name='post-detail')
]