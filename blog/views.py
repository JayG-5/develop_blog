
import json

from django.shortcuts import render, redirect
from django.db.models import Q
from django.views import View
from django.contrib import messages
from .models import Post,Hashtag,Like,Image,Profile,Follow
from .forms import UserProfileForm,ImageUploadForm
from .decorators import user_has_permission
from .utils.image import upload_image,handle_markdown_images

# Create your views here.

class Index(View):    
    def get(self, request):
        def get_posts(query):
            if query:
                if query.startswith('#'):
                    hashtags = Hashtag.objects.filter(Q(name__icontains=query[1:]))
                    hashtag_to_post = hashtags.values_list('post',flat=True)
                    raw_posts = Post.objects.filter(Q(pk__in=hashtag_to_post))
                elif query.startswith('@'):
                    profiles = Profile.objects.filter(Q(nickname__icontains=query[1:]))
                    if len(profiles) == 1:
                        raise Exception(profiles.first().nickname)
                    raw_posts = Post.objects.filter(Q(user__nickname__icontains=query[1:])).distinct()
                else:
                    search_conditions = Q(title__icontains=query) | Q(body__icontains=query) | Q(user__nickname__icontains=query)
                    raw_posts = Post.objects.filter(search_conditions).distinct()
            else:
                raw_posts = Post.objects.all()
            return [{
                        'post' : post,
                        'hashtag' :post.hashtag_set.all(), 
                        'like' :post.like_set.all(), 
                        'thumbnail' :Image.objects.filter(file_id=post.thumbnail),
                    } for post in raw_posts.order_by('-created_at')]
        
        def get_context(query):
            context = {
                'posts': get_posts(query),
            }
            if query:
                context['query'] = query
            return context
        
        try:
            query = request.GET.get('q')
            return render(request, 'blog/index.html', get_context(query))
        except Exception as e:
            return redirect('blog:user',e)

    

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
        if request.user.is_authenticated:
            context['is_like'] = bool(likes.filter(user = request.user).first())
        return render(request, 'blog/post-view.html', context)
    
    @user_has_permission(['login'])
    def post(self, request, pk):
        parent = Post.objects.get(pk=pk)
        title = f'[Re]: {parent.title}'
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
                parent_post = parent
            )
            messages.success(request, '글이 성공적으로 작성되었습니다.')
            return redirect('blog:detail',pk = pk)   
        except :
            messages.error(request, '글 작성에 실패했습니다.')
        return redirect('blog:index')
    


class WriteView(View):
    
    @user_has_permission(['login'])
    def get(self, request):
        return render(request, 'blog/editor_form.html')
        
        
    @user_has_permission(['login'])
    def post(self, request):
        title = request.POST.get('title', '')
        body = handle_markdown_images(request.POST.get('body', ''))
        print(request.POST)
        print(title)
        print(body)
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
            'hashtag' :post.hashtag_set.all(), 
            'like' :post.like_set.all(), 
            'thumbnail' :Image.objects.filter(file_id=post.thumbnail),
        } for post in Post.objects.filter(user = profile).order_by('-created_at')]
        
        hashtags = Hashtag.objects.filter(Q(post__user=profile)).values_list('name',flat=True).distinct()
        print(hashtags)

        context = {
            'posts': posts,
            'profile': profile,
            'hashtags': hashtags,
            'social':profile_social,
        }
        if request.user.is_authenticated:
            context['is_follow'] = bool(Follow.objects.filter(followed_user = profile.user,following_user = request.user).first)
        return render(request, 'blog/index.html', context)
        
    
class HashTagSearch(View):
    
    def get(self, request, hashtag):
        hashtags = Hashtag.objects.filter(name__icontains = hashtag)
        hashtag_to_post = hashtags.values_list('post',flat=True)
        
        post_ = Post.objects.filter(pk__in=hashtag_to_post)
        posts = [{
            'post' : post,
            'hashtag' :post.hashtag_set.all(), 
            'like' :post.like_set.all(), 
            'thumbnail' :Image.objects.filter(file_id=post.thumbnail),
        } for post in post_]
        
        context = {
            'posts': posts,
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
    
    
class UserFollow(View):
    
    @user_has_permission(['login','not_me'])
    def post(self,request,nickname):
        profile = Profile.objects.get(nickname = nickname)
        try:
            follow = Follow.objects.get(following_user = request.user,followed_user = profile.user)
            follow.delete()
        except:
            follow = Follow.objects.create(
                following_user = request.user,
                followed_user = profile.user
            )
        return redirect('blog:user', nickname = nickname)


class PostLike(View):
    
    @user_has_permission(['login'])
    def post(self,request,pk):
        post = Post.objects.get(pk = pk)
        try:
            like = Like.objects.get(post = post, user = request.user)
            like.delete()
        except:
            like = Like.objects.create(
                post = post, 
                user = request.user
            )
        return redirect('blog:detail', pk = pk)

class PostHashtag(View):
    
    @user_has_permission(['login','own'])
    def post(self,request,pk):
        post = Post.objects.get(pk = pk)

        def check_existence(name):
            try:
                return Hashtag.objects.get(post = post, name = name)
            except:
                return False

        name = request.POST.get('name')
        method = request.POST.get('method')

        is_exists = check_existence(name)

        if method == 'add' and not is_exists:
            Hashtag.objects.create(
                post = post,
                name = name,
            )
        if method == 'remove' and is_exists:
            is_exists.delete()
        return redirect('blog:detail', pk = pk)
