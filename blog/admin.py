from django.contrib import admin
from django import forms
from django.utils.html import format_html
from .models import Post,Image,Profile,Like,Follow,Hashtag
from markdownx.admin import MarkdownxModelAdmin

class ImageAdmin(admin.ModelAdmin):
    list_display = ('file_id', 'thumbnail', 'created_at')
    list_display_links = ('file_id',)

    def thumbnail(self, obj):
        return format_html(f'<img src="{obj.image.url}" width="100" height="100" />')

    thumbnail.allow_tags = True
    

class LikeInline(admin.TabularInline):
    model = Like
    extra = 0
    readonly_fields = ['user', 'created_at']


class HashtagInline(admin.TabularInline):
    model = Hashtag
    extra = 1


class PostAdmin(admin.ModelAdmin):
    inlines = [LikeInline, HashtagInline]
    list_display = ['title', 'user']
    search_fields = ['title', 'user__email']


admin.site.register(Image, ImageAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Profile)
admin.site.register(Hashtag)
admin.site.register(Follow)
