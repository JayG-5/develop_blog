from django.db import models
from django.contrib.auth import get_user_model
from django.core.serializers import json
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils.safestring import mark_safe


User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=16, unique=True, blank=False,default=f'{User.last_name}{User.first_name}')
    bio = models.CharField(max_length=100, blank=True)
    profile_image = models.ForeignKey('Image', on_delete=models.SET_NULL, null=True, blank=True)
    social_accounts = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.nickname


class Follow(models.Model):
    following_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    followed_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.following_user.username} follow -> {self.followed_user.username}'


class Image(models.Model):
    file_id = models.CharField(max_length=100, primary_key=True)
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file_id
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    body = MarkdownxField()
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    thumbnail = models.ForeignKey(Image,on_delete=models.SET_NULL, null=True,blank=True, related_name='post_thumbnail')
    parent_post = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='child_posts')
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def get_markdown_body(self):
        return mark_safe(markdownify(self.body))


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} likes {self.post.title}'


class Hashtag(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=12)

    def __str__(self):
        return self.name