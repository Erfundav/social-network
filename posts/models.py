from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
class Post(models.Model):
    user = models.ForeignKey(to=User, related_name='%(class)ss', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    caption = models.TextField(blank=True, null=True, max_length=2048)
    is_active = models.BooleanField(default=True)
    is_public = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        db_table = 'post'
        
    def __str__(self):
        return f'{self.id}-{self.title}'
    
  
class PostFile(models.Model):
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='%(class)ss')
    file = models.FileField()
  
    class Meta:
        verbose_name = 'post file'
        verbose_name_plural = 'post files'
        db_table = 'post file'
  
    
class Comment(models.Model):
    post = models.ForeignKey(to=Post, related_name='comments', on_delete=models.PROTECT)
    user = models.ForeignKey(to=User, related_name='comments', on_delete=models.CASCADE)
    parent = models
    text = models.TextField()
    is_approved = models.BooleanField(default=False)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        db_table = 'comment'


class Like(models.Model):
    post = models.ForeignKey(to=Post, related_name='likes', on_delete=models.PROTECT)
    user = models.ForeignKey(to=User, related_name='likes', on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'like'
        verbose_name_plural = 'likes'
        db_table = 'like'
    