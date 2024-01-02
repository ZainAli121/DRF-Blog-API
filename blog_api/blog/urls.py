from . import views
from django.urls import path

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('post-list/', views.postlist, name="post-list"),
]