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
    
    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', None)

        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.image = validated_data.get('image', instance.image)

        if tags_data is not None:
            instance.tags.clear()
            for tag_data in tags_data:
                tag_name = tag_data.get('name', None)
                if tag_name:
                    tag, created = Tag.objects.get_or_create(name=tag_name)
                    instance.tags.add(tag)

        instance.save()
        return instance
   
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'