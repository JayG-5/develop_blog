
import json

from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from .models import Post,Hashtag,Like,Image,Profile
from .forms import UserProfileForm,ImageUploadForm
from .decorators import user_has_permission
from .utils import upload_image,handle_markdown_images

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
    


class WriteView(View):
    
    @user_has_permission(['login'])
    def get(self, request):
        return render(request, 'blog/editor_form.html')
        
        
    @user_has_permission(['login'])
    def post(self, request):
        title = request.POST.get('title', '')
        body = handle_markdown_images(request.POST.get('body', ''))
        try:
            thumbnail = body[1][0]
        except:
            thumbnail = None
        try:
            post = Post.objects.create(
                title=title,
                body=body[0],
                user=request.user.profile, 
                thumbnail = thumbnail, 
            )
            messages.success(request, '글이 성공적으로 작성되었습니다.')
            return redirect('blog:detail',pk = post.pk)   
        except:
            messages.error(request, '글 작성에 실패했습니다.')
        return redirect('blog:index')
    

class UpdateView(View):
    
    @user_has_permission(['login','own'])
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        context = {
            'post': post,
        }
        return render(request, 'blog/editor_form.html',context)
        
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        title = request.POST.get('title', '')
        body = handle_markdown_images(request.POST.get('body', ''))
        try:
            thumbnail = body[1][0]
        except:
            thumbnail = None
        try:
            post.title = title
            post.body = body[0]
            post.thumbnail = thumbnail
            post.save()
            messages.success(request, '글이 성공적으로 수정되었습니다.')
            return redirect('blog:detail',pk = post.pk)   
        except:
            messages.error(request, '글 수정에 실패했습니다.')
        return redirect('blog:index')



class PostDelete(View):

    @user_has_permission(['login','own'])
    def post(self, request, pk):
        post = Post.objects.get(pk=pk)
        if post.user == request.user.profile:
            messages.success(request, '글이 성공적으로 삭제되었습니다.')
            post.delete()
        return redirect('blog:index')
        
        

class UserView(View):
    
    def get(self, request, nickname):
        profile = Profile.objects.get(nickname = nickname)
        profile_social = {}
        try:
            profile_social = json.loads(profile.social_accounts)
        except:
            profile_social = {}

        posts = [{
            'post' : post,
            'hashtag' :Hashtag.objects.filter(post=post), 
            'like' :Like.objects.filter(post=post), 
            'thumbnail' :Image.objects.filter(file_id=post.thumbnail),
        } for post in Post.objects.filter(user = profile).order_by('-created_at')]
        context = {
            'posts': posts,
            'profile': profile,
            'social':profile_social,
        }
        return render(request, 'blog/index.html', context)
        
    


class EditProfileView(View):

    @user_has_permission(['login','own'])
    def get(self, request, nickname):
        profile = Profile.objects.get(nickname=nickname)
        form = UserProfileForm(instance=profile)
        image_form = ImageUploadForm(instance=profile.profile_image if profile.profile_image else None)
        context = {
            'form': form,
            'image': image_form,
            'nickname' : nickname
        }
        return render(request, 'blog/profile_edit.html', context)
        
        
    @user_has_permission(['login','own'])
    def post(self, request,nickname):
        profile = Profile.objects.get(nickname = nickname)
        form = UserProfileForm(request.POST)
        image_form = ImageUploadForm(files=request.FILES)

        if image_form.is_valid():
            image = image_form.cleaned_data.get('image', False)
            if image:
                profile.profile_image = upload_image(image);

        if form.is_valid():
            profile.nickname = form.cleaned_data['nickname']
            profile.bio =form.cleaned_data['bio']

        profile.save()

        return redirect('blog:user', nickname = profile.nickname)