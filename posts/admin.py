from django.contrib import admin

from .models import *


class PostFileInLine(admin.TabularInline):
    model = PostFile
    fields = ['id', 'file']
    extra = 0
    can_delete = False
    can_change = False
    can_add = False
    
    
class CommentInLine(admin.TabularInline):
    model = Comment
    fields = ['user', 'text', 'is_approved']
    extra = 0
        
    
class LikeInLine(admin.TabularInline):
    model = Like
    fields = ['user', 'is_liked']
    extra = 0
    
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'is_active', 'is_public', 'created_time']
    inlines = [PostFileInLine, CommentInLine, LikeInLine]
    list_filter = ['is_active', 'is_public']
    search_fields = ['title']
    
