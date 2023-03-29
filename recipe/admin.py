from django.contrib import admin
from .models import Recipe, Comment


@admin.register(Recipe)
class Admin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created', 'rate', 'num_people']
    prepopulated_fields = {'slug': ('title', )}


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'recipe', 'created', 'active']
    list_filter = ['active', 'created', 'updated']
    search_fields = ['name', 'email', 'commentaire']
    
