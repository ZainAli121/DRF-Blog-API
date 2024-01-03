from rest_framework import serializers
from .models import Tag, Post, Comment
from django.contrib.auth.models import User

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'

    def create(self, validated_data):
        tags_data = validated_data.pop('tags', [])
        post = Post.objects.create(**validated_data)

        for tag_data in tags_data:
            tag_name = tag_data.get('name', None)
            if tag_name:
                tag, created = Tag.objects.get_or_create(name=tag_name)
                post.tags.add(tag)
        
        return post
   
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'