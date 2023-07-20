from django.shortcuts import render,redirect
from django.views import View
from blog.models import Profile
from .utils.nickname import generate_random_sentence
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login


class Registration(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:index')
        # 회원가입 페이지
        # 정보를 입력할 폼을 보여주어야 한다.
        form = RegisterForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/user_register.html', context)
    
    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('user:login')
        

class Login(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('blog:index')
        
        form = LoginForm()
        context = {
            'form': form,
            'title': 'User'
        }
        return render(request, 'user/user_login.html', context)
        
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('blog:index')
        
        form = LoginForm(request, request.POST)
        if form.is_valid():
            email = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password) # True, False
            
            if user:
                login(request, user)
                try:
                    user_profile = Profile.objects.get(user=request.user)
                    return redirect('blog:index')
                except Profile.DoesNotExist:
                    new_nickname = ''
                    try:
                        while True:
                            new_nickname = generate_random_sentence()
                            Profile.objects.get(nickname = new_nickname)
                    except:
                        new_profile = Profile.objects.create(
                            user=request.user, 
                            nickname=new_nickname,
                        )   
                    return redirect('blog:edit',nickname = new_nickname)
            
        form.add_error(None, '아이디가 없습니다.')
        
        context = {
            'form': form
        }
        
        return render(request, 'user/user_login.html', context)
