from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
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
        
    
class UserView(View):
    
    def get(self, request, nickname):
        profile = Profile.objects.get(nickname = nickname)
        post = 
        
        posts = [{
            'post' : post,
            'hashtag' :Hashtag.objects.filter(post=post), 
            'like' :Like.objects.filter(post=post), 
            'thumbnail' :Image.objects.filter(file_id=post.thumbnail),
        } for post in post.objects]
        context = {
            'posts': posts,
        }
        return render(request, 'blog/index.html', context)
        
    

class WriteView(View):
    
    def get(self, request):
        context = {
        }
        return render(request, 'blog/editor_form.html', context)
        
        
    def post(self, request):
        title = request.POST.get('title', '')  # 에디터에서 입력한 제목
        body = request.POST.get('body', '')    # 에디터에서 입력한 본문
        try:
            post = Post.objects.create(
                title=title,
                body=body,
                user=request.user.profile,  # 로그인된 유저의 Profile을 가져와서 연결합니다.
                # 나머지 필드들도 필요한 정보로 채워줍니다.
            )
            messages.success(request, '글이 성공적으로 작성되었습니다.')
            return redirect('blog:detail',pk = post.pk)   
        except:
            messages.error(request, '글 작성에 실패했습니다.')
        return redirect('blog:index')
