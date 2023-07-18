from django.shortcuts import render
from django.views import View
from .models import Post,Hashtag,Like,Image,Profile


# Create your views here.

class Index(View):
    
    def get(self, request):
        posts = [{
            'post' : post,
            'hashtag' :Hashtag.objects.filter(post=post), 
            'like' :Like.objects.filter(post=post), 
            'thumbnail' :Image.objects.filter(file_id=post.thumbnail),
        } for post in Post.objects.order_by('-created_at')]
        context = {
            'posts': posts,
        }
        return render(request, 'blog/index.html', context)
    

class DetailView(View):
    
    def get(self, request, pk):
        post = Post.objects.get(pk = pk)
        comments = Post.objects.filter(parent_post = post)
        hashtags = post.hashtag_set.all()
        likes =  post.like_set.all()
        
        context = {
            'post': post,
            'comments': comments,
            'hashtags': hashtags,
            'likes': likes,
        }
        return render(request, 'blog/post-view.html', context)
        
        