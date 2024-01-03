from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/post-list-create/',
        'Detail View': '/post-detail/<str:pk>/',
        'Update': '/post-update/<str:pk>/',
        'Delete': '/post-delete/<str:pk>/',
        }
    return Response(api_urls)

@api_view(['GET', 'POST'])
def postlist(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(auther=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)