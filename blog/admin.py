from django.contrib import admin
from .models import Category, Post, Tag, Comment
from mptt.admin import MPTTModelAdmin


class CategoryAdmin(MPTTModelAdmin):
    '''категории'''
    mptt_level_indent = 20
    prepopulated_fields = {'slug': ('name',)}


class PostAdmin(admin.ModelAdmin):
    '''посты'''
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Comment)


