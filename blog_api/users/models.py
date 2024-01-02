from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True)
    tags = models.ManyToManyField(Tag, null=True)
    image = models.ImageField(null=True, default='default.jpg')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at','-created_at']

    def __str__(self):
        return f'{self.auther} - {self.title}'
    

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True)
    auther = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    body = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated_at','-created_at']
        
    def __str__(self):
        return f'{self.auther} - {self.post.title}'
